from django import forms
from .models import SavingTarget, Saving

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
    class Meta:
        model = SavingTarget
        fields = ['target_name', 'amount']


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
        )
    )
    
    class Meta:
        model = Saving
        fields = ['amount', 'target']
