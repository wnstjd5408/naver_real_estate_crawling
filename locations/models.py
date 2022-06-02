from turtle import Turtle

from django.db import models
from pyexpat import model


# Create your models here.
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)
    count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id)


class Apartment(models.Model):
    id = models.AutoField(primary_key=True)
    apt_name = models.CharField(max_length=300)
    apt_dong = models.CharField(max_length=30, null=True)
    apt_transaction_type = models.CharField(max_length=15)
    apt_price = models.CharField(max_length=300)
    apt_category = models.CharField(max_length=15)
    apt_flat = models.FloatField()
    apt_real_flat = models.FloatField()
    apt_height = models.CharField(max_length=50, null=True)
    apt_wind = models.CharField(max_length=30, null=True)
    apt_comment = models.TextField(null=True)
    apt_feature = models.TextField(null=True)
    apt_confirm = models.CharField(max_length=50)
    apt_confirm_date = models.DateField()
    apt_link = models.URLField(max_length=500, null=True, blank=True)
    apt_regiseter = models.DateTimeField(null=True)
    apt_change_price = models.BigIntegerField(null=True)
    location_id = models.name = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id)
