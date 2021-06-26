from django.contrib import admin

from .models import BootCamp, BootCampRegister


@admin.register(BootCamp)
class BootCampAdmin(admin.ModelAdmin):
    pass


@admin.register(BootCampRegister)
class BootCampRegisterAdmin(admin.ModelAdmin):
    list_display = ['bootcamp', 'phone', 'completed_payment']
    list_filter = ['bootcamp', 'completed_payment']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
