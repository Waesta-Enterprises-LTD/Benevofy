from django import forms
from .models import Biodata, Dependent


class BiodataForm(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = '__all__'
        exclude = ['member', 'dependents']

    def __init__(self, *args, **kwargs):
        super(BiodataForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'


class DependentForm(forms.ModelForm):
    class Meta:
        model = Dependent
        fields = '__all__'
        exclude = ['biodata', 'dependent_to']

    def __init__(self, *args, **kwargs):
        super(DependentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'