from rest_framework import serializers
from .models import RenterAd, PictureAdRenter, Vehicle, Buckets, PhoneAd, AdditionalEquipment, TypeService
from users.models import MyUser


class PictureAdSerializer(serializers.ModelSerializer):
    img_ads = serializers.ImageField(required=True)

    class Meta:
        model = PictureAdRenter
        fields = "img_ads",


class AdditionalEquipmentSerializer(serializers.ModelSerializer):
    # vehicle_additionalequipment = serializers.StringRelatedField(many=True)

    class Meta:
        model = AdditionalEquipment
        fields = "description",


class RenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"


class PhoneAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneAd
        fields = "phone_ad_renter",


class BucketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buckets
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    renter = serializers.HiddenField(default=serializers.CurrentUserDefault())
    vehicle_buckets = serializers.PrimaryKeyRelatedField(queryset=Buckets.objects.all(), many=True)
    vehicle_additional_equipment = serializers.PrimaryKeyRelatedField(queryset=AdditionalEquipment.objects.all(),
                                                                      many=True)

    class Meta:
        model = Vehicle
        fields = "__all__"

    def create(self, validated_data):
        vehicle_buckets = validated_data.pop('vehicle_buckets', None)
        vehicle_additional_equipment = validated_data.pop('vehicle_additional_equipment', None)

        instance = super().create(validated_data)
        if vehicle_buckets:
            instance.vehicle_buckets.add(*vehicle_buckets)
        if vehicle_additional_equipment:
            instance.vehicle_additional_equipment.add(*vehicle_additional_equipment)

        return instance


class VehicleFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super().get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(renter=request.user)


class RenterAdSerializer(serializers.ModelSerializer):
    abs_url = serializers.SerializerMethodField()
    renter_ad = serializers.HiddenField(default=serializers.CurrentUserDefault())

    vehicle_ad = VehicleFilteredPrimaryKeyRelatedField(queryset=Vehicle.objects.all(), many=False)
    types_of_services = serializers.PrimaryKeyRelatedField(queryset=TypeService.objects.all(), many=True)

    class Meta:
        model = RenterAd
        fields = '__all__'

    def create(self, validated_data):
        types_of_services = validated_data.pop('types_of_services', None)
        image_data = self.context['request'].FILES
        list_image = []
        instance = super().create(validated_data)
        if image_data:
            for key, value in image_data.items():
                serializer = PictureAdSerializer(data={'img_ads': value})
                if serializer.is_valid():
                    list_image.append(PictureAdRenter(img_ads=value, ad_link=instance))
                if list_image:
                    PictureAdRenter.objects.bulk_create(list_image)
        obj_list_type_service = []
        for obj_tps in types_of_services:
            try:
                type_service_obj = TypeService.objects.get(pk=obj_tps.pk)
            except TypeService.DoesNotExist:
                continue
            obj_list_type_service.append(type_service_obj)

        instance.types_of_services.add(*obj_list_type_service)
        return instance

    def get_abs_url(self, obj):
        return obj.get_absolute_url()
