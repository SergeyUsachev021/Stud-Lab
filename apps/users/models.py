from django.contrib.auth.models import AbstractUser
from django.db import models

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
    pass

class BuyerProfile(BaseProfile):
    pass