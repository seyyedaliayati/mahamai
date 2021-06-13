from django.db import models
from django.forms.fields import EmailField


class ContactUs(models.Model):
    full_name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.full_name}"

    class Meta:
        verbose_name_plural = "Contact Us Data"


class workwithus(models.Model):
    subject = models.CharField(max_length=20)
    first_name = models.CharField(max_length=130)
    last_name = models.CharField(max_length=130)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    upload_file = models.FileField

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.phone}"
