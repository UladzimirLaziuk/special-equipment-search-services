import pytest
from django.urls import reverse

from rentor_app.models import PictureAdRenter


@pytest.mark.django_db
def test_create_vehicle(data_vehicle_with_additional_buckets, auth_client, user):
    response = auth_client.post(reverse('create_obj_vehicle'), data=data_vehicle_with_additional_buckets)
    assert response.status_code == 201


@pytest.mark.django_db
def test_file_create_ad_and_upload_picture(auth_client, ads_data, img_dict):
     response = auth_client.post(reverse('create_ads'),
        data= {**img_dict, **ads_data},
    )
     assert response.status_code == 201
     assert len(img_dict) == PictureAdRenter.objects.count()



