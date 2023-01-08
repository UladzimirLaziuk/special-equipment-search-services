from io import StringIO
import io

import pytest
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from pytest_mock import mocker
from rest_framework.test import APIClient
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


#
# @pytest.fixture
# def data_file_post(img_file):
#     image_name = "fake-image-stream.jpg"
#     video_name = "fake-video-stream.mp4"
#     docs_name = "fake-docs-stream.pdf"
#
#     # response = self.client.post(url, {'file': imgfile})
#
#     data_file = {
#         "title": "string",
#         "topic_title": 1,
#         "picturepost_set": [{'image_post': img_file},
#                             {'image_post': img_file},
#                             ],
#         "description": "string",
#         'post_owner': 1,
#         # "videopost_set": [{'video_post': SimpleUploadedFile(video_name, b"abc", content_type="video/webm")},
#         #                   {'video_post': SimpleUploadedFile(video_name, b"abc", content_type="video/webm")},
#         #                   ],
#         # "docpost_set": [{'doc_post': SimpleUploadedFile(docs_name, b"abc", content_type="text/plain")},
#         #                 {'doc_post': SimpleUploadedFile(docs_name, b"abc", content_type="text/plain")}
#         #                 ]
#     }
#
#     return data_file
#


@pytest.mark.django_db
def client():
    return APIClient()


@pytest.fixture
def auth_client(user, client):
    client.force_login(user)
    return client


@pytest.fixture
def data_user():
    data = dict(email='test4@mail.com',
                password='admin',
                first_name='john',
                last_name='Lennon',
                status=1)
    return data


@pytest.fixture
@pytest.mark.django_db
def user(data_user):
    return models.MyUser.objects.create_user(**data_user)
