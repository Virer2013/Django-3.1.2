from django.contrib.auth.models import User
from django import forms
from pizzashopapp.models import PizzaShop

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserFormFormEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PizzaShopForm(forms.ModelForm):
    class Meta:
        model = PizzaShop
        fields = ('name', 'phone', 'address', 'logo')
