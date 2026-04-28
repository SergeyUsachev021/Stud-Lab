from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.users import models


@admin.register(models.User)
class UserAdmin(ModelAdmin):
    pass

@admin.register(models.SellerProfile)
class SellerProfileAdmin(ModelAdmin):
    pass

@admin.register(models.BuyerProfile)
class BuyerProfileAdmin(ModelAdmin):
    pass
