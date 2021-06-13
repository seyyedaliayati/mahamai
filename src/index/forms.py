from django import forms

from .models import ContactUs, WorkWithUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'


class WorkWithUsForm(forms.ModelForm):
    class Meta:
        model = WorkWithUs
        fields = '__all__'
