from django import forms
from .models import Withdraw

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = ['phone', 'names' ,'amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Phone number'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Amount', 'type': 'number', 'min': '500'})
        self.fields['names'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Account Names', 'required': True})