from django.shortcuts import render
from .forms import LoanRequestForm

def request_loan(request):
    member = request.user.member
    form = LoanRequestForm()
    if request.method == 'POST':
        amount = request.POST.get('amount')
        interest_rate = request.POST.get('interest_rate')
        repayment_date = request.POST.get('repayment_date')
        LoanRequest.objects.create(
            user=member,
            amount=amount,
            interest_rate=interest_rate,
            repayment_date=repayment_date
        )
        return render(request, 'benevofy/request_loan.html', {'member': member})
    return render(request, 'benevofy/request_loan.html', {'member': member, 'form': form})