from datetime import datetime
from django.db import models


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
