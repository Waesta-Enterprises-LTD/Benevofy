from django import forms
from .models import Poll, Candidate, Constitution

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'poll_type', 'closing_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'closing_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'poll_type': forms.Select(attrs={'class': 'form-control mb-3'}),
        }

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['member']
        widgets = {
            'member': forms.Select(attrs={'class': 'form-control mb-3'}),
        }


class ConstitutionForm(forms.ModelForm):
    class Meta:
        model = Constitution
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }

