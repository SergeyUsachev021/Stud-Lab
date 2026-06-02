from django.contrib import admin

from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.labs import models


@admin.register(models.Lab)
class LabAdmin(ModelAdmin):
    pass


@admin.register(models.LabFile)
class LabFileAdmin(ModelAdmin):
    pass


@admin.register(models.ArchivedLab)
class ArchivedLabAdmin(ModelAdmin):
    list_display = ('user', 'lab', 'created_at')
    search_fields = ('user__username', 'lab__name')