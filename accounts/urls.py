from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("basket/", BasketListView.as_view(), name="balist"),
    # path("basket/create/", BasketAddView.as_view(), name="bacreate"),
]
