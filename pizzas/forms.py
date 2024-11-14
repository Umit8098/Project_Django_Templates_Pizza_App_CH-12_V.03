from django import forms
from .models import Order

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'size',
            'quantity',
        )
        widgets = {
            'size':forms.RadioSelect,
            'quantity':forms.TextInput(attrs={'class':'rounded border border-warning form-control', 'style':'width:50%'}),
        }
