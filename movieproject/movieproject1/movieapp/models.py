from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=250)
    details=models.TextField()
    year=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name