from django.contrib import admin

from .models import Apartment, Location

# Register your models here.


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    search_fields = ["apt_name"]
    list_display = ["id", "apt_name", "apt_dong"]
    list_per_page = 30


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ["location_name"]
    list_display = ["id", "location_name"]
