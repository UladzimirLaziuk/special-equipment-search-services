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
def test_destroy_user(data_user, client):
    response = client.delete(reverse('update-destroy-profiles'), data=data_user)


@pytest.mark.django_db
def test_update_user(data_user, client):
    response = client.put(reverse('update-destroy-profiles'), data=data_user)


@pytest.mark.django_db
def test_set_image_profiles_user(data_user, client):
    response = client.put(reverse('set_image_profiles'), data=data_user)
