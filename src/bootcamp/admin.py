from django.contrib import admin

from .models import BootCamp, BootCampRegister


@admin.register(BootCamp)
class BootCampAdmin(admin.ModelAdmin):
    pass


@admin.register(BootCampRegister)
class BootCampRegisterAdmin(admin.ModelAdmin):
    pass
