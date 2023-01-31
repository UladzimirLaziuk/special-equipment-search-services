from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveAPIView

from tenants_app.models import SearchTable
from tenants_app.serializers import SearchRentorSerializer


class SearchRentorCreateView(CreateAPIView):
    queryset = SearchTable
    serializer_class = SearchRentorSerializer


class SearchRentorRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = SearchTable
    serializer_class = SearchRentorSerializer


class SearchRentorDeleteView(DestroyAPIView):
    queryset = SearchTable
    serializer_class = SearchRentorSerializer


class SearchRentorDetailView(RetrieveAPIView):
    queryset = SearchTable
    serializer_class = SearchRentorSerializer
