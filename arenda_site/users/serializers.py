from django.core.validators import EmailValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import MyUser


class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = 'first_name', 'last_name', 'email', 'password', 'status'
        # extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


class ProfileImageSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MyUser
        fields = 'owner', 'profile_image',


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = 'email', 'password'
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': [EmailValidator]},
        }
