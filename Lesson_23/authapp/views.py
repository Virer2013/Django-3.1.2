from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authapp.forms import UserForm, PizzaShopForm

# Create your views here.
def home(request):
    return redirect(authapp_home)

@login_required(login_url='/authapp/login')
def authapp_home(request):
    return render(request, 'authapp/home.html', {})

def authapp_sign_up(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()
    return render(request, 'authapp/sign_up.html', {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form
    })
