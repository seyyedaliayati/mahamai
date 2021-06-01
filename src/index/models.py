from django.db import models


class ContactUs(models.Model):
    full_name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.full_name}"


class WorkWithUs(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    service = models.CharField(max_length=32)  # choice field
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
