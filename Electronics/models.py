from django.db import models
from django.db.models import Model


class Mobile(models.Model):
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=30)
    Ram = models.IntegerField()
    Price = models.FloatField()
    image_url = models.CharField(max_length=2083, null=True)


class EarBuds(models.Model):
    Company = models.CharField(max_length=255)
    Model_Name = models.CharField(max_length=255)
    Version = models.CharField(max_length=10)
    Noise_Cancellation = models.BooleanField()
    Cost = models.FloatField()



