from django import forms
from .models import LoanRequest

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = LoanRequest
        fields = ('recieving_number', 'amount', 'guarantors', 'repayment_date')
        widgets = {
            'repayment_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(LoanRequestForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'


