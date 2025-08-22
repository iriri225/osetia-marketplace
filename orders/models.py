from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('confirmed', 'Подтверждён'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупатель")
    shop = models.ForeignKey('shops.Shop', on_delete=models.CASCADE, verbose_name="Магазин")
    total = models.DecimalField("Сумма", max_digits=10, decimal_places=2)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='new')
    address = models.CharField("Адрес доставки", max_length=200)
    phone = models.CharField("Телефон", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ {self.id} — {self.user.username}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Количество")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
