from django.contrib import admin

from .models import ContactUs, WorkWithUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', ]
    search_fields = ['email', 'full_name', 'message', ]


@admin.register(WorkWithUs)
class WorkWithUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'subject', ]
    search_fields = ['email', 'first_name', 'last_name', 'message', ]
