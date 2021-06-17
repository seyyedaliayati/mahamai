from django.db import models
from django_jalali.db import models as jmodels


class BootCamp(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    main_photo = models.FileField(upload_to='bootcamp/')
    start_date = jmodels.jDateField(blank=True, null=True)
    end_date = jmodels.jDateField(blank=True, null=True)

    is_presence = models.BooleanField(default=False)
    is_hybrid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
