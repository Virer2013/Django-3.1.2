from django.db import models

# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пиццерия')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='интернет-адрес пиццерии')

    class Meta:
        verbose_name='Пиццерия'
        verbose_name_plural='Пиццерии'

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название пиццы')
    short_description = models.CharField(max_length=30, verbose_name='Краткое описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    photo = models.ImageField('Фото', upload_to='firstapp/photos', default='',blank=True)

    class Meta:
        verbose_name='Пицца'
        verbose_name_plural='Пиццы'
        ordering = ['name']

    def __str__(self):
        return self.name
