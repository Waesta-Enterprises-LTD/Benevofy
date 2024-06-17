from django.forms import ModelForm
from django import forms
from .models import Loan, LoanRepayment


class LoanRepaymentForm(ModelForm):
    class Meta:
        model = LoanRepayment
        fields = ['loan', 'amount']
        widgets = {
            'loan': forms.Select(attrs={'class': 'form-control mb-3'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        }
