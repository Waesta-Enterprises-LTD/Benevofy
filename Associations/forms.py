from .models import Association
from django import forms


class SettingForm(forms.ModelForm):
    class Meta:
        model = Association
        fields = [
            'website',
            'email',
            'phone',
            'address',
            'loan_interest_rate',
            'minimum_monthly_savings',
            'registration_fee'
        ]

    def __init__(self, *args, **kwargs):
        super(SettingForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'


