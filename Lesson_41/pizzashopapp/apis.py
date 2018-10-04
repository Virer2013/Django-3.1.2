from django.http import JsonResponse

from .models import PizzaShop
from pizzashopapp.serializers import PizzaShopSerializer

def client_get_pizzashops(request):
    pizzashops = PizzaShopSerializer(
        PizzaShop.objects.all().order_by('-id'),
        many=True,
        context={'request':request}
    ).data

    return JsonResponse({'pizzashops': pizzashops})
