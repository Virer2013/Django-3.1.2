from django.shortcuts import render
from firstapp.models import Pizza

# Create your views here.
def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})
