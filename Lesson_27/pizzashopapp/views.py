from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return redirect(pizzashop_home)

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_home(request):
    return render(request, 'pizzashop/home.html', {})

def pizzashop_sign_up(request):
    return render(request, 'pizzashop/sign_up.html', {})
