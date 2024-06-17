from django.shortcuts import render, redirect
from .models import Saving, SavingTarget
from .forms import SavingTargetForm, SavingForm
from django.db.models import Q
from uuid import uuid4
import requests


def save_money(request):
    member = request.user.member
    form = SavingForm()
    if member:
        form.fields['target'].queryset = SavingTarget.objects.filter(Q(association=member.logged_in_association) | Q(user=member))
    if request.method == 'POST':
        form = SavingForm(request.POST)
        reference = str(uuid4())
        if form.is_valid():
            form.instance.association = member.logged_in_association
            form.instance.user = member
            form.instance.reference = reference
            saving = form.save()
        target = form.cleaned_data['target']
        target.savings.add(saving)
        phone = request.POST.get('phone')
        amount = form.cleaned_data['amount']
        if phone.startswith('256'):
            currency = 'UGX'
        elif phone.startswith('254'):
            currency = 'KES'
        else:
            return render(request, 'benevofy/save_money.html', {'member': member, 'error': 'Invalid phone number. The number should have a country code.', 'form': form})
        url = "https://payments.relworx.com/api/mobile-money/request-payment"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/vnd.relworx.v2",
            "Authorization": "Bearer ec719b1a0db84d.YNrIn4iWVanw1Y0ptYvrVA"
        }
        payload = {
            "account_no": member.logged_in_association.rel_account,
            "reference": reference,
            "msisdn": '+'+phone,
            "currency": currency,
            "amount": int(amount),
            "description": f"{target.target_name} Savings"
        }
        response = requests.request("POST", url, headers=headers, json=payload)
        print(response.json())
        return redirect('payment_initiated')
    return render(request, 'benevofy/save_money.html', {'member': member, 'form': form})


def create_saving_target(request):
    if request.method == 'POST':
        form = SavingTargetForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user.member
            form.save()
            return redirect('view_savings')
    else:
        form = SavingTargetForm()
    return render(request, 'benevofy/create_saving_target.html', {'form': form})

def view_savings(request):
    saving_targets = SavingTarget.objects.filter(Q(association=request.user.member.logged_in_association) | Q(user=request.user.member))
    return render(request, 'benevofy/view_savings.html', {'saving_targets': saving_targets})


def view_target_savings(request, target_id):
    target = SavingTarget.objects.get(pk=target_id)
    savings = target.savings.all()
    return render(request, 'benevofy/view_target_savings.html', {'target': target, 'savings': savings})

