from typing import List

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *
from locations.models import Apartment

from accounts.forms import BasketForm

from .models import Basket

# Create your views here.


class BasketListView(ListView):
    model = Basket
    template_name = "accounts/basketlist.html"
    context_object_name = "ba"

    def get_context_data(self, **kwarg):
        label = []
        price = []
        user = self.request.user
        queryset = Basket.objects.filter(uIDX=user).select_related("aIDX")

        context = super().get_context_data(queryset=queryset)
        for ba in queryset:
            label.append(ba.aIDX.apt_name)
            price.append(ba.aIDX.apt_change_price)
            print(ba.aIDX.apt_change_price)
            print(ba.aIDX.apt_name)
        context["name"] = label
        context["price"] = price

        return context

    # def get_queryset(self):
    #     user = self.request.user
    #     return Basket.objects.filter(uIDX=user).select_related("aIDX")


# @method_decorator(login_required, name="dispatch")
# class BasketAddView(CreateView):
#     model = Basket
#     fields = "__all__"
#     success_url = reverse_lazy("location:aptdetail")
#     template_name: str = "location/aptdetail.html"

#     def form_valid(self, form):
#         form.instance.uIDX = self.request.user
#         return super(BasketAddView, self).form_valid(form)
