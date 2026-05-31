from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.labs import models


@admin.register(models.Lab)
class LabAdmin(ModelAdmin):
    pass

@admin.register(models.LabFile)
class LabFileAdmin(ModelAdmin):
    pass