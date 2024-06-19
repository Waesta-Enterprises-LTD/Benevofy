from django import forms
from .models import SavingTarget, Saving, NormalSaving

class SavingTargetForm(forms.ModelForm):
    target_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Target name'
            }
        )
    )
    amount = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Amount'
            }
        )
    )

    target_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Target date',
                'type': 'date'
            }
        )
    )

    class Meta:
        model = SavingTarget
        fields = ['target_name', 'amount', 'target_date']


class SavingForm(forms.ModelForm):
    amount = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Amount'
            }
        )
    )

    target = forms.ModelChoiceField(
        queryset=SavingTarget.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control mb-3'
            }
        ),
        required=False
    )
    
    class Meta:
        model = Saving
        fields = ['amount', 'target']


class NormalSavingForm(forms.ModelForm):
    amount = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Amount'
            }
        )
    )

    class Meta:
        model = NormalSaving
        fields = ['amount']