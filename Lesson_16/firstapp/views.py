from django.shortcuts import render, get_object_or_404
from firstapp.models import Pizza

# Create your views here.
def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return render(request, 'pizza_detail.html', {'pizza': pizza})
