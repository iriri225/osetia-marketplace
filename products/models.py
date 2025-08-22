from django.db import models

from django.db import models
from shops.models import Shop

class Category(models.Model):
    name = models.CharField("Категория", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Магазин")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Фото", upload_to="products/")
    stock = models.PositiveIntegerField("Остаток", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
