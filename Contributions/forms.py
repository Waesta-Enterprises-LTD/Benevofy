from django import forms
from Events.models import Event
from .models import EventContribution, PersonalEventContribution


class ContributeEventForm(forms.Form):
    events = forms.ModelMultipleChoiceField(
        queryset=Event.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )


class ContributionForm(forms.ModelForm):
    class Meta:
        model = EventContribution
        fields = ['event', 'amount']
        widgets = {
            'event': forms.Select(attrs={'class': 'form-control mb-3'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        }


class PersonalContributionForm(forms.ModelForm):
    class Meta:
        model = PersonalEventContribution
        fields = ['names' ,'email', 'phone', 'amount']
        widgets = {
            'names': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Names', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email Address', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Phone Number', 'required': True}),
            'amount': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Amount', 'required':True}),
        }

