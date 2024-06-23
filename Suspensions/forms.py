from django import forms
from .models import Suspension


class SuspensionForm(forms.ModelForm):
    class Meta:
        model = Suspension
        fields = '__all__'
        exclude = ['user', 'association', 'status']
        widgets = {
            'till': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
