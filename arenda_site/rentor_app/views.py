from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveAPIView

from . import models
from .serializers import RenterAdSerializer, VehicleSerializer


class AdRenterCreateView(CreateAPIView):
    queryset = models.RenterAd
    serializer_class = RenterAdSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class VehicleRenterCreateView(CreateAPIView):
    queryset = models.Vehicle
    serializer_class = VehicleSerializer


class AdRenterUpdateView(UpdateAPIView):
    pass


class AdRenterDeleteView(DestroyAPIView):
    pass


class AdRenterDetailView(RetrieveAPIView):
    pass
