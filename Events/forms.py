from django import forms
from django.db import models
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['contributions', 'status']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.DateInput):
                field.widget.input_type = 'date'
                field.widget.attrs['class'] = 'form-control mb-3 datepicker'
                field.widget.attrs['data-provide'] = 'datepicker'
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.input_type = 'time'
                field.widget.attrs['class'] = 'form-control mb-3 timepicker'
                field.widget.attrs['data-provide'] = 'timepicker'
            elif isinstance(field.widget, forms.DateTimeInput):
                field.widget.input_type = 'datetime-local'
                field.widget.attrs['class'] = 'form-control mb-3 datetimepicker'
                field.widget.attrs['data-provide'] = 'datetimepicker'
            else:
                field.widget.attrs['class'] = 'form-control mb-3'



