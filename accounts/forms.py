from dataclasses import fields

from django import forms
from django.db import models

from .models import Basket


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        exclude = ["aIDX", "uIDX"]
