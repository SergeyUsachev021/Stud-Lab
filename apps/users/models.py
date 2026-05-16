from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    yandex_id = models.BigIntegerField(blank=True, null=True)

class BaseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    class Meta:
        abstract = True


class SellerProfile(BaseProfile):
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_sales = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Seller: {self.name}"


class BuyerProfile(BaseProfile):
    total_purchases = models.IntegerField(default=0)
    favorite_categories = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Buyer: {self.name}"