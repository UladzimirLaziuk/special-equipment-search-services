import pytest
from django.urls import reverse
from rentor_app.models import PictureAdRenter, RenterAd


@pytest.mark.django_db
def test_create_vehicle(data_vehicle_with_additional_buckets, auth_client, user):
    response = auth_client.post(reverse('create_obj_vehicle'), data=data_vehicle_with_additional_buckets)
    assert response.status_code == 201


@pytest.mark.django_db
def test_file_create_ad_and_upload_picture(auth_client, ads_data, img_dict):
    response = auth_client.post(reverse('create_ads'),
                                data={**img_dict, **ads_data}, format='multipart',
                                )
    assert response.status_code == 201
    assert len(img_dict) == PictureAdRenter.objects.count()


@pytest.mark.django_db
def test_ads_update_patch(ads_create, auth_client):
    dict_update = {'title': 'Test update'}
    response = auth_client.patch(reverse('renter_ad_update', args=[str(ads_create.pk)]),
                                 data=dict_update, content_type='application/json',
                                 )
    assert response.status_code == 200


@pytest.mark.django_db
def test_ads_update_put(ads_create, ads_data, auth_client, img_dict):
    ads_data_put = ads_data.copy()
    dict_update = {'title': 'Test update'}
    ads_data_put.update(dict_update)
    ads_data_put.pop('types_of_services')
    response = auth_client.put(reverse('renter_ad_update', args=[str(ads_create.pk)]),
                               data=ads_data_put, content_type='application/json',
                               )
    assert response.status_code == 200


@pytest.mark.django_db
def test_ads_destroy(ads_create, auth_client):
    response = auth_client.delete(reverse('renter_ad_update', args=[str(ads_create.pk)]))
    assert response.status_code == 204
