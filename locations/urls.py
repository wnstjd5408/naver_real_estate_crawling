from django.urls import path

from .views import *

app_name = "location"

urlpatterns = [
    path("", LocationListView.as_view(), name="idx"),
    path("<int:pk>", LocationDetailView.as_view(), name="detail"),
    path('apartment/<int:pk>', ApartmentDetailView.as_view(), name='aptdetail'),    
]
