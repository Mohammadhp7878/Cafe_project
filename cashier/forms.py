from django import forms
from orders.models import Product_Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Product_Order
        fields = "__all__"
