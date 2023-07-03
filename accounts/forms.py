from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from orders.models import Order

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
