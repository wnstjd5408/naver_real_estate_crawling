from django.views.generic import *

from .models import Apartment, Location

# Create your views here.


class LocationListView(ListView):
    template_name = "location/locationlist.html"
    context_object_name = "locationlist"
    model = Location

    def get_queryset(self):
        return Location.objects.order_by("id")


class LocationDetailView(DetailView):

    template_name = "location/aptlist.html"
    context_object_name = "aptlist"

    model = Location
    paginate_by = 12

    def get_context_data(self, **kwargs):
        object_list = Apartment.objects.filter(location_id=self.get_object())

        context = super().get_context_data(object_list=object_list, **kwargs)

        context["location"] = Location.objects.filter(id=self.kwargs["pk"])
        return context
