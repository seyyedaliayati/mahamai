from django.contrib import admin

from .models import BootCamp


@admin.register(BootCamp)
class BootCampAdmin(admin.ModelAdmin):
    pass
