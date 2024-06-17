from django.shortcuts import render
from .models import Loan

def view_loans(request):
    loans = Loan.objects.all()
    return render(request, 'benevofy/view_loans.html', {'loans': loans})

def apply_for_loan(request):
    return render(request, 'benevofy/apply_for_loan.html')