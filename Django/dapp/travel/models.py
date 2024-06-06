from django.db import models

# Create your models here.

class Destination(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()