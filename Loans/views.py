from django.shortcuts import render, redirect
from .models import Loan
from .forms import LoanRepaymentForm
from uuid import uuid4
import requests

def view_loans(request):
    loans = Loan.objects.all()
    return render(request, 'benevofy/view_loans.html', {'loans': loans})

def apply_for_loan(request):
    return render(request, 'benevofy/apply_for_loan.html')

def repay_loan(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    form = LoanRepaymentForm(initial={'loan': loan})
    member = request.user.member
    if request.method == 'POST':
        reference = str(uuid4())
        form = LoanRepaymentForm(request.POST, initial={'loan': loan})
        print(form.errors)
        if form.is_valid():
            form.instance.reference = reference
            form.instance.user = loan.user
            form.save()
            phone = request.POST.get('phone')
            amount = form.cleaned_data['amount']
            if phone.startswith('256'):
                currency = 'UGX'
            elif phone.startswith('254'):
                currency = 'KES'
            else:
                return render(request, 'benevofy/repay_loan.html', {'member': member, 'error': 'Invalid phone number. The number should have a country code.', 'form': form})
            url = "https://payments.relworx.com/api/mobile-money/request-payment"
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/vnd.relworx.v2",
                "Authorization": "Bearer ec719b1a0db84d.YNrIn4iWVanw1Y0ptYvrVA"
            }
            payload = {
                "account_no": loan.association.rel_account,
                "reference": reference,
                "msisdn": '+'+phone,
                "currency": currency,
                "amount": int(amount),
                "description": f"Loan Repayment #{loan.id}"
            }
            response = requests.request("POST", url, headers=headers, json=payload)
            print(response.json())
            return redirect('payment_initiated')
    form.fields['loan'].disabled = True
    return render(request, 'benevofy/repay_loan.html', {'loan': loan, 'form': form})


def loan_payments(request, loan_id):
    return render(request, 'benevofy/loan_payments.html')