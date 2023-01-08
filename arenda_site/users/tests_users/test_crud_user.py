import pytest
from django.urls import reverse
from users import models

@pytest.mark.django_db
def test_create_user(data_user, client):
    response = client.post(reverse('create-profiles'), data=data_user)
    assert response.status_code == 201
    email = data_user.get('email')
    assert email == models.MyUser.objects.get(email=email).email

@pytest.mark.django_db
def test_destroy_user(data_user, auth_client):
    response = auth_client.delete(reverse('update-destroy-profiles'), data=data_user)
    assert response.status_code  == 204


@pytest.mark.django_db
def test_update_user(data_user, auth_client):
    dict_update = dict(first_name = 'Yoko')
    response = auth_client.patch(reverse('update-destroy-profiles'),
                                 data=dict_update, content_type='application/json',)
    assert response.status_code == 200


@pytest.mark.django_db
def test_set_image_profiles_user(data_user, auth_client, img_file):
    response = auth_client.post(reverse('set_image_profiles'), {'profile_image':img_file})
    assert response.status_code == 200
