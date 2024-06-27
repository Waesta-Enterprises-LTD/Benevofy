from django.shortcuts import render, redirect
from .forms import WithdrawForm
from .models import Withdraw
from uuid import uuid4
from django.core.mail import send_mail
import requests

def view_withdraws(request):
    form = WithdrawForm()
    return render(request, 'benevofy/view_withdraws.html', {'form': form})


def make_withdraw(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user.member
            form.instance.association = request.user.member.logged_in_association
            withdraw = form.save()
            request.user.member.withdraws.add(withdraw)
            return redirect('view_withdraws')


def reject_withdraw(request, withdraw_id):
    withdraw = Withdraw.objects.get(id=withdraw_id)
    reason = request.POST.get('reason')
    withdraw.reason_for_rejection = reason
    withdraw.status = 'Rejected'
    withdraw.save()
    # send email
    subject = f'Withdraw request rejected - {withdraw.association.name}'
    message = f'Withdraw request with amount of {withdraw.amount} has been rejected. Reason: {reason}'
    from_email = f'{request.user.member.logged_in_association.name} <info@benevofy.net>'
    recipient_list = [withdraw.user.user.email]
    send_mail(subject, message, from_email, recipient_list)
    return redirect('view_withdraws')



def approve_withdraw(request, withdraw_id):
    withdraw = Withdraw.objects.get(id=withdraw_id)
    reference = uuid4()
    # call RelWorx API to initiate payment
    api_url = 'https://payments.relworx.com/api/mobile-money/send-payment'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.relworx.v2',
        'Authorization': 'Bearer ec719b1a0db84d.YNrIn4iWVanw1Y0ptYvrVA'
    }
    data = {
        "account_no": request.user.member.logged_in_association.rel_account,
        "reference": str(reference),
        "msisdn": '+'+withdraw.phone,
        "currency": "UGX",
        "amount": int(withdraw.amount),
        "description": f"Send Payment to {withdraw.user.user.get_full_name()}."
    }
    response = requests.post(api_url, headers=headers, json=data)
    response = response.json()
    print(response)
    if response['success']:
        withdraw.status = 'Approved'
        withdraw.reference = str(reference)
        withdraw.save()
    return redirect('view_withdraws')



def cancel_withdraw(request, withdraw_id):
    withdraw = Withdraw.objects.get(id=withdraw_id)
    withdraw.delete()
    return redirect('view_withdraws')
