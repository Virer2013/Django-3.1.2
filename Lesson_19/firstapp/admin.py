from django.contrib import admin
from firstapp.models import PizzaShop, Pizza, Order
# Register your models here.
admin.site.register(PizzaShop)
admin.site.register(Pizza)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pizza', 'name', 'phone', 'date']
