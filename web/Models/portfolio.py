from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='images')
