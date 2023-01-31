from rest_framework import serializers

from tenants_app.models import SearchTable


class SearchRentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchTable
        fields = "__all__"