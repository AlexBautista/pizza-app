from django import forms
from .models import Order

class Orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customername','sinstructions','pizza_flavor']