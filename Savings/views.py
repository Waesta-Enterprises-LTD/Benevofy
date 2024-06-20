from django.shortcuts import render, redirect
from .models import Saving, SavingTarget
from .forms import SavingTargetForm, SavingForm, NormalSavingForm
from django.db.models import Q
from uuid import uuid4
import requests


def save_money(request, target_id):
    member = request.user.member
    target = SavingTarget.objects.get(id=target_id)
    form = SavingForm(initial={'target': target})
    form.fields['target'].widget.attrs['disabled'] = True
    if request.method == 'POST':
        form = SavingForm(request.POST, initial={'target': target})
        form.fields['target'].widget.attrs['disabled'] = True
        reference = str(uuid4())
        if form.is_valid():
            form.instance.association = member.logged_in_association
            form.instance.user = member
            form.instance.reference = reference
            form.instance.target = target
            saving = form.save()
        else:
            print(form.errors)
        target.savings.add(saving)
        member.savings.add(saving)
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
        response = response.json()
        if response['success']:
            return redirect('payment_initiated')
        else:
            saving.delete()
            form = SavingForm(initial={'target': target})
            form.fields['target'].widget.attrs['disabled'] = True
            return render(request, 'benevofy/save_money.html', {'member': member, 'error': 'Failed to initiate payment. Please contact support.', 'form': form})
    return render(request, 'benevofy/save_money.html', {'member': member, 'form': form})


def create_saving_target(request):
    if request.method == 'POST':
        form = SavingTargetForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user.member
            form.save()
            return redirect('save_money', target_id=form.instance.id)
    else:
        form = SavingTargetForm()
    return render(request, 'benevofy/create_saving_target.html', {'form': form})

def view_savings(request):
    saving_targets = SavingTarget.objects.filter(user=request.user.member)
    return render(request, 'benevofy/view_savings.html', {'saving_targets': saving_targets})


def view_target_savings(request, target_id):
    target = SavingTarget.objects.get(pk=target_id)
    savings = target.savings.all()
    return render(request, 'benevofy/view_target_savings.html', {'target': target, 'savings': savings})


def normal_saving(request):
    form = NormalSavingForm()
    form.fields['amount'].widget.attrs['min'] = request.user.member.logged_in_association.minimum_monthly_savings
    if request.method == 'POST':
        phone = request.POST.get('phone')   
        form = NormalSavingForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            reference = str(uuid4())
            form.instance.association = request.user.member.logged_in_association
            form.instance.member = request.user.member
            form.instance.reference = reference
            saving = form.save()
            request.user.member.logged_in_association.savings.add(saving)
        phone = request.POST.get('phone')
        if phone.startswith('256'):
            currency = 'UGX'
        elif phone.startswith('254'):
            currency = 'KES'
        else:
            return render(request, 'benevofy/save_money.html', {'member': request.user.member, 'error': 'Invalid phone number. The number should have a country code.', 'form': form})
        url = "https://payments.relworx.com/api/mobile-money/request-payment"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/vnd.relworx.v2",
            "Authorization": "Bearer ec719b1a0db84d.YNrIn4iWVanw1Y0ptYvrVA"
        }
        payload = {
            "account_no": request.user.member.logged_in_association.rel_account,
            "reference": reference,
            "msisdn": '+'+phone,
            "currency": currency,
            "amount": int(amount),
            "description": f"Normal Savings"
        }
        response = requests.request("POST", url, headers=headers, json=payload)
        response = response.json()
        if response['success']:
            return redirect('payment_initiated')
        else:
            saving.delete()
            return render(request, 'benevofy/normal_saving.html', {'form': form, 'error': 'Failed to initiate payment. Please contact support.'})
    return render(request, 'benevofy/normal_saving.html', {'form': form})


def delete_target(request, target_id):
    target = SavingTarget.objects.get(pk=target_id)
    target.delete()
    return redirect('view_savings')