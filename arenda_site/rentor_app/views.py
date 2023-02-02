from functools import reduce

import django_filters

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, \
    RetrieveAPIView, ListAPIView

from . import models
from .serializers import RenterAdSerializer, VehicleSerializer, RenterAdUpdateSerializer, SearchRenterAdSerializer
from django_filters import rest_framework as filters
import operator


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


class RenterAdFilter(django_filters.FilterSet):
    price_per_hour_from__gte = django_filters.NumberFilter(field_name='price_per_hour_from', lookup_expr='gte')
    price_per_hour_to__lte = django_filters.NumberFilter(field_name='price_per_hour_to', lookup_expr='lte')

    price_per_shift_from__gte = django_filters.NumberFilter(field_name='price_per_shift_from', lookup_expr='gte')
    price_per_shift_from__lte = django_filters.NumberFilter(field_name='price_per_shift_from', lookup_expr='lte')

    weight_from__gte = django_filters.NumberFilter(field_name='vehicle_ad__weight', lookup_expr='gte')
    weight_from__lte = django_filters.NumberFilter(field_name='vehicle_ad__weight', lookup_expr='lte')

    vehicle_ad__vehicle_buckets__width = django_filters.CharFilter(method='filter_by_width_buckets_fields')

    @classmethod
    def filter_by_width_buckets_fields(cls, queryset, name, value):
        list_buckets = value.split(',')
        list_query = [queryset.filter(**{name: width}) for width in list_buckets if width]
        return reduce(operator.or_, list_query)

    class Meta:
        model = models.RenterAd
        fields = ('price_per_hour_from__gte', 'price_per_hour_to__lte',
                  'price_per_shift_from__gte', 'price_per_shift_from__lte',
                  'min_work_time', 'region_work',
                  'weight_from__gte', 'weight_from__lte', 'vehicle_ad__vehicle_buckets__width')


class SearchRenterAdListViews(ListAPIView):
    queryset = models.RenterAd.objects.all()
    serializer_class = SearchRenterAdSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RenterAdFilter
