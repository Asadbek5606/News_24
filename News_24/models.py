from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    offer = models.BooleanField(default=False)
    
class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    