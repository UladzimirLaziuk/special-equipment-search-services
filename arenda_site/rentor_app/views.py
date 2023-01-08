from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveAPIView

from . import models
from .serializers import RenterAdSerializer, VehicleSerializer, RenterAdUpdateSerializer


class AdRenterCreateView(CreateAPIView):
    queryset = models.RenterAd
    serializer_class = RenterAdSerializer


class VehicleRenterCreateView(CreateAPIView):
    queryset = models.Vehicle
    serializer_class = VehicleSerializer


class AdRenterRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = models.RenterAd
    serializer_class = RenterAdUpdateSerializer


class AdRenterDeleteView(DestroyAPIView):
    pass


class AdRenterDetailView(RetrieveAPIView):
    pass
