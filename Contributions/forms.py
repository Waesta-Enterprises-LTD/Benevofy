from django import forms
from Events.models import Event
from .models import EventContribution


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

