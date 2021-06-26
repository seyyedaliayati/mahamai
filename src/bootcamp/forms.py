from django import forms

from .models import BootCampRegister


class BootCampRegisterForm(forms.ModelForm):
    class Meta:
        model = BootCampRegister
        fields = ["first_name", "last_name", "email", "phone", "want_virtual"]
