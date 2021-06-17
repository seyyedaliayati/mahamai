from django.db import models

class BootCamp(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    pictures = models.FileField(upload_to='../templates/bootcamp/bootcamp_images/' , blank=True, null=True)
    start_date= models.DateField()
    end_date= models.DateField()
    presence_status = models.BooleanField(default=False)
    not_presence_status = models.BooleanField(default=False)
    hybrid_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title}"