from django.shortcuts import render

def view_loans(request):
    return render(request, 'benevofy/view_loans.html')

def apply_for_loan(request):
    return render(request, 'benevofy/apply_for_loan.html')