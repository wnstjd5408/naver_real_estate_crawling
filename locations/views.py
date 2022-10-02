from typing import List

from accounts.forms import BasketForm
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import *
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin

from .models import Apartment, Location

# Create your views here.


class LocationListView(ListView):
    template_name = "location/locationlist.html"
    context_object_name = "locationlist"
    model = Location

    def get_queryset(self):
        return Location.objects.order_by("id")


class ApartmentSearchList(ListView):
    model = Apartment
    context_object_name = "aptlist"
    template_name: str = "location/aptSearchList.html"
    paginate_by = 20

    def get_queryset(self):
        val = self.request.GET.get("search", "")
        location = self.request.GET.get("location", "")
        if val:
            queryset = Apartment.objects.filter(Q(apt_name__contains=val), location=location).distinct()
        else:
            queryset = Apartment.objects.filter(location=location)
        return queryset


class LocationDetailView(MultipleObjectMixin, DetailView):

    template_name = "location/aptlist.html"
    context_object_name = "aptlist"

    model = Location
    paginate_by = 20

    def get_context_data(self, **kwargs):
        object_list = Apartment.objects.filter(location=self.get_object())

        context = super().get_context_data(object_list=object_list, **kwargs)

        context["location"] = Location.objects.filter(id=self.kwargs["pk"])
        return context


class ApartmentDetailView(FormMixin, DetailView):
    model = Apartment
    template_name = "location/aptdetail.html"
    context_object_name = "apartment"
    form_class = BasketForm

    def get_success_url(self):
        return reverse("location:aptdetail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        bookmark.aIDX = get_object_or_404(Apartment, pk=self.object.pk)
        bookmark.uIDX = self.request.user
        bookmark.save()
        return super(ApartmentDetailView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
