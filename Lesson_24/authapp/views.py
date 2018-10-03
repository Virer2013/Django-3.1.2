from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authapp.forms import UserForm, PizzaShopForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return redirect(authapp_home)

@login_required(login_url='/authapp/login')
def authapp_home(request):
    return render(request, 'authapp/home.html', {})

def authapp_sign_up(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES)

        if user_form.is_valid() and pizzashop_form.is_valid():

            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizzashop = pizzashop_form.save(commit=False)
            new_pizzashop.user = new_user
            new_pizzashop.save()

            user = authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            )

            login(request, user)

            return redirect(authapp_home)

    return render(request, 'authapp/sign_up.html', {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form
    })
