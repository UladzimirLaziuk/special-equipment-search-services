from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, profile_picture=None, password=None, is_admin=False, is_staff=True,
                    is_active=True, first_name=None, last_name=None, status=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        # if not full_name:
        #     raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.last_name = last_name
        user.first_name = first_name
        user.set_password(password)  # change password to hash
        user.profile_picture = profile_picture
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name=None, profile_picture=None, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)
        user.profile_picture = profile_picture
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractUser):

    class StatusUsers(models.TextChoices):
        Rent = "1", "Rentor"
        Cust = "2", "Customer"


    status = models.CharField(
        max_length=2,
        choices=StatusUsers.choices,
        default=StatusUsers.Rent
    )
    email = models.EmailField(_('email address'), unique=True)
    profile_image = models.ImageField(upload_to='profile_image', default='default.jpg', blank=True)
    phone = PhoneNumberField(blank=True)
    name_company = models.CharField(max_length=50, default='', blank=True)
    user_position = models.CharField(max_length=50, default='', blank=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'status']
    objects = UserManager()

    class Meta:
        verbose_name = "App User"
        verbose_name_plural = "App Users"

    @property
    def get_full_name(self):
        if self.username:
            return '%s. %s' % (self.username[:1], self.last_name)
        return '%s. %s' % (self.first_name[:1], self.last_name)

    # def get_absolute_url(self):
    #     return reverse('profiles-detail', args=[str(self.pk)])

    # def __str__(self):
    #     return '%s. %s' % (self.username[:1], self.last_name)