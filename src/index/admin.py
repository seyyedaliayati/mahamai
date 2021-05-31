from django.contrib import admin

from index.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'service', ]
    list_filter = ['service', ]
    search_fields = ['email', 'first_name', 'last_name', ]
