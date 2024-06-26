from django import forms
from .models import Pledge


class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = ['email', 'phone', 'amount', 'due_date']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Phone Number'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Amount'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control mb-3 datepicker', 'data-provide': 'datepicker', 'type': 'date'}),
        }