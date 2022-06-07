from django.db import models
from django.urls import reverse


# Create your models here.
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)
    count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = "위치"
        verbose_name_plural = f"{verbose_name} 목록"
        ordering = ["-id"]


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
    apt_register = models.DateTimeField(null=True)
    apt_change_price = models.BigIntegerField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("location:aptdetail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return "%s %s %s" % (str(self.id), self.apt_name, self.apt_dong)

    class Meta:
        verbose_name = "아파트"
        verbose_name_plural = f"{verbose_name} 목록"
        ordering = ["id"]
