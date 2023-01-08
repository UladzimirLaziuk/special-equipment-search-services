import io

import pytest
from PIL import Image
from rest_framework.test import APIClient

from rentor_app.models import Buckets, AdditionalEquipment, Vehicle, TypeService, RenterAd, PictureAdRenter
from users import models
from django.core.files import File


@pytest.fixture
def img_file():
    size = (50, 50)
    color = (256, 0, 0)
    file_obj = io.BytesIO()
    image = Image.new("RGBA", size=size, color=color)
    image.save(file_obj, 'png')
    file_obj.seek(0)
    return File(file_obj, name='test.png')


@pytest.fixture
def img_dict(img_file):
    t = 3
    return {'file' + str(i): img_file for i in range(t)}


@pytest.mark.django_db
def client():
    return APIClient()


@pytest.fixture
@pytest.mark.django_db
def types_service():
    list_name = ['Рытье траншей', 'Монтаж колодцев']
    list_obj = [TypeService(type_work=name) for name in list_name]
    list_obj_create = TypeService.objects.bulk_create(list_obj)

    return list_obj_create


@pytest.fixture
def data_user():
    data = dict(email='test4@mail.com',
                password='admin',
                first_name='John',
                last_name='Lennon',
                status=1)
    return data


@pytest.fixture
@pytest.mark.django_db
def user(data_user):
    return models.MyUser.objects.create_user(**data_user)


@pytest.fixture
def auth_client(user, client):
    client.force_login(user)
    return client


@pytest.fixture
def data_vehicle(user):
    data = dict(name_brand='JCB',
                renter=user,
                weight=2.5,
                max_digging_depth=2.5,
                vehicle_height=2.35,
                )
    return data


@pytest.fixture
def data_vehicle_with_additional_buckets(data_vehicle):
    vehicle_additional_equipment = 'Отбойник', 'Бур'
    vehicle_buckets = 40, 35
    vehicle_buckets_list = [Buckets(width=width) for width in vehicle_buckets]
    Buckets.objects.bulk_create(vehicle_buckets_list)

    vehicle_additional_equipment_list = [AdditionalEquipment(description=description) for description in
                                         vehicle_additional_equipment]
    AdditionalEquipment.objects.bulk_create(vehicle_additional_equipment_list)
    dt_vehicle = data_vehicle.copy()
    dt_vehicle.update({'vehicle_buckets': Buckets.objects.values_list('id', flat=True),
                       'vehicle_additional_equipment': AdditionalEquipment.objects.values_list('id', flat=True)})
    return dt_vehicle


@pytest.fixture
def vehicle(data_vehicle):
    obj = Vehicle.objects.create(**data_vehicle)
    list_vehicle_buckets = Buckets.objects.values_list('id', flat=True)
    list_additional_equipment = AdditionalEquipment.objects.values_list('id', flat=True)
    obj.vehicle_additional_equipment.add(*list_additional_equipment)
    obj.vehicle_buckets.add(*list_vehicle_buckets)
    return obj


@pytest.fixture
def ads_data(user, vehicle, types_service):
    data = dict(
        title="Тест объявление",
        renter_ad=user.id,
        vehicle_ad=vehicle.id,
        description='Текст описание объявления',
        price_per_hour_from="40.05",
        price_per_hour_to="45.09",
        price_per_shift_from='200.06',
        price_per_shift_to='320.0',
        min_work_time=4,
        work_weekends_time='Круглосуточно',
        work_time="",
        place_work="",
        region_work="",
        delivery="",
        types_of_services=TypeService.objects.values_list('id', flat=True),
    )
    return data


@pytest.fixture
def ads_create(ads_data, img_dict, types_service):
    ads_user_data = ads_data.copy()
    ads_user_data['renter_ad'] = models.MyUser.objects.get(pk=ads_data['renter_ad'])
    ads_user_data['vehicle_ad'] = Vehicle.objects.get(pk=ads_data['vehicle_ad'])
    ads_user_data.pop('types_of_services')
    dict_ads = {**ads_user_data}
    ads = RenterAd.objects.create(**dict_ads)
    list_image = [PictureAdRenter(img_ads=img, ad_link=ads) for img in img_dict]
    if list_image:
        PictureAdRenter.objects.bulk_create(list_image)
    return ads