from django.shortcuts import render, redirect
from .forms import LoanRequestForm
from .models import LoanRequest
from Loans.models import Loan

def request_loan(request):
    member = request.user.member
    form = LoanRequestForm()
    if request.method == 'POST':
        form = LoanRequestForm(request.POST)
        if form.is_valid():
            receiver_number = form.cleaned_data['recieving_number']
            receiver_number = str(receiver_number)
            if receiver_number.startswith('256') or receiver_number.startswith('254'):
                form.instance.member = member
                form.instance.association = member.logged_in_association
                form.instance.user = member
                form.save()
                return redirect('view_loans')
            else:
                return render(request, 'benevofy/request_loan.html', {'member': member, 'error': 'Invalid phone number. The number should have a country code.', 'form': form})
    return render(request, 'benevofy/request_loan.html', {'member': member, 'form': form})


def view_loan_requests(request):
    requests = LoanRequest.objects.filter(association=request.user.member.logged_in_association)
    return render(request, 'benevofy/view_loan_requests.html', {'requests': requests})


def approve_loan_request(request, request_id):
    loan_request = LoanRequest.objects.get(id=request_id)
    loan_request.status = 'Approved'
    loan_request.save()
    loan = Loan(
        user=request.user.member,
        association=loan_request.association,
        amount=loan_request.amount,
        interest_rate=request.user.member.logged_in_association.loan_interest_rate,
        repayment_date=loan_request.repayment_date,
    )
    loan.save()
    return redirect('view_loans')