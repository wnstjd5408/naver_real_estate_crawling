from django.urls import path

from .views import *

app_name = "location"

urlpatterns = [
    path("", LocationListView.as_view(), name="idx"),
]
