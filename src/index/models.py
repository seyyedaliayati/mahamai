from django.db import models


class ContactUs(models.Model):
    full_name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.full_name}"

    class Meta:
        verbose_name_plural = "Contact Us Data"

    def get_ull_name(self):
        return self.full_name


class WorkWithUs(models.Model):
    subject = models.CharField(max_length=20)
    first_name = models.CharField(max_length=130)
    last_name = models.CharField(max_length=130)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    resume_file = models.FileField(upload_to='work-with-us/', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Work with Us Data"

    def get_ull_name(self):
        return f"{self.first_name} {self.last_name}"
