from datetime import datetime
from django.db import models
from django.urls import reverse


class BootCamp(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    # TODO: Add page content here
    price = models.PositiveIntegerField()
    main_photo = models.FileField(upload_to='bootcamp/')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    is_presence = models.BooleanField(default=False)
    is_hybrid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-start_date', )

    def __str__(self) -> str:
        return self.title

    def can_enroll(self):
        return self.start_date > datetime.now().date()

    def get_absolute_url(self):
        return reverse('bootcamp_detail', kwargs={'pk': self.pk})

    def get_register_url(self):
        return reverse('bootcamp_register', kwargs={'pk': self.pk})


class BootCampRegister(models.Model):
    bootcamp = models.ForeignKey(BootCamp, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=130)
    last_name = models.CharField(max_length=130)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    want_virtual = models.BooleanField(default=False)
    payment_ref_id = models.CharField(default="No Ref ID", max_length=128)
    completed_payment = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created', )

    def __str__(self):
        return f"{self.bootcamp} - {self.phone}"

    def get_callback_url(self):
        return reverse('bootcamp_register_verify', kwargs={'pk': self.pk})
