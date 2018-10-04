from rest_framework import serializers
from pizzashopapp.models import PizzaShop, Pizza

class PizzaShopSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    def get_logo(self, pizzashop):
        request = self.context.get('request')
        logo_url = pizzashop.logo.url
        return request.build_absolute_uri(logo_url)
    class Meta:
        model = PizzaShop
        fields = ('id', 'name', 'phone', 'address', 'logo')

class PizzaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, pizza):
        request = self.context.get('request')
        image_url = pizza.image.url
        return request.build_absolute_uri(image_url)
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'short_description', 'image', 'price')
