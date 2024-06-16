from django import forms
from .models import Poll, Candidate

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'closing_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'closing_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
        }

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['member']
        widgets = {
            'member': forms.Select(attrs={'class': 'form-control mb-3'}),
        }


