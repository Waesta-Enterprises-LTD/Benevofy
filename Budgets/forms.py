from django.forms import ModelForm
from .models import Budget, Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'