from rest_framework import serializers
from pizzashopapp.models import PizzaShop

class PizzaShopSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    def get_logo(self, pizzashop):
        request = self.context.get('request')
        logo_url = pizzashop.logo.url
        return request.build_absolute_uri(logo_url)
    class Meta:
        model = PizzaShop
        fields = ('id', 'name', 'phone', 'address', 'logo')
