from django import forms
from orders.models import Product_Order , Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Product_Order
        fields = "__all__"


class StatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

