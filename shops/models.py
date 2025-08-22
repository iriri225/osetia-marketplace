from django.db import models

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Shop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Владелец")
    name = models.CharField("Название магазина", max_length=100)
    description = models.TextField("Описание", blank=True)
    phone = models.CharField("Телефон", max_length=20)
    address = models.CharField("Адрес", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"