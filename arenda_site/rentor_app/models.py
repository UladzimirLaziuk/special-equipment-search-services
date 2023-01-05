from django.db import models
from phonenumber_field.formfields import PhoneNumberField

from users.models import MyUser
from django.urls import reverse
from sorl.thumbnail import ImageField

class TypeService(models.Model):
    type_work = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.type_work}'


class Vehicle(models.Model):
    name_brand = models.CharField(max_length=255, blank=True)
    renter = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True, default=None)

    max_digging_depth = models.FloatField(null=True, blank=True, default=0.0)
    vehicle_height = models.FloatField(null=True, blank=True, default=0.0)
    vehicle_additional_equipment = models.ManyToManyField('AdditionalEquipment', blank=True)
    vehicle_buckets = models.ManyToManyField('Buckets', blank=True)

    def __str__(self):
        return f'{self.name_brand}'


class Buckets(models.Model):
    description = models.CharField(max_length=100, default='Ковш')
    width = models.PositiveIntegerField(verbose_name='Ширина ковша')

    class Meta:
        ordering = ('width',)


class AdditionalEquipment(models.Model):
    description = models.CharField(max_length=100)
    params = models.PositiveIntegerField(verbose_name='Параметр оборудования', blank=True, null=True)


class RenterAd(models.Model):
    title = models.CharField(max_length=255)
    renter_ad = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    vehicle_ad = models.ForeignKey(Vehicle, on_delete=models.CASCADE)#TODO ONE TO ONE
    description = models.TextField()

    price_per_hour_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    price_per_hour_to = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)

    price_per_shift_from = models.FloatField(null=True, blank=True, default=None)
    price_per_shift_to = models.FloatField(null=True, blank=True, default=None)

    min_work_time = models.PositiveIntegerField(blank=True, null=True, default=0)
    work_weekends_time = models.CharField(max_length=255, blank=True, null=True)
    work_time = models.CharField(max_length=255, blank=True, null=True)
    place_work = models.CharField(max_length=255, blank=True, null=True)
    region_work = models.CharField(max_length=255, blank=True, null=True)  # TODO Many to many
    delivery = models.CharField(max_length=255, blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата публикации')
    types_of_services = models.ManyToManyField('TypeService', blank=True)

    def get_absolute_url(self):
        return reverse('renter_ad_detail', args=[str(self.pk)])


class PhoneAd(models.Model):
    ad_renter = models.ForeignKey(RenterAd, on_delete=models.CASCADE)
    phone_ad_renter = PhoneNumberField()


class PictureAdRenter(models.Model):
    ad_link = models.ForeignKey(RenterAd, on_delete=models.CASCADE)
    img_url = models.URLField(verbose_name='Фото url объявления', default='')
    smile_img_url = models.URLField(verbose_name='Фото smile url объявления', blank=True, null=True)
    img_ads = ImageField(upload_to='image/', default="")
