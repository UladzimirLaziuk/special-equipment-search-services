from django.db import models
from django.utils import timezone
from rentor_app.models import TypeService
from users.models import MyUser

# Create your models here.
def one_day_hence():
    return timezone.localtime() + timezone.timedelta(days=1)

class SearchTable(models.Model):
    client_renter = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_start_period_work = models.DateTimeField(default=timezone.localtime)  # period must
    date_end_period_work = models.DateTimeField(default=one_day_hence)
    location = models.CharField(max_length=100)
    estimated_working_time = models.TimeField(verbose_name="Прeдполагаемое время работ", blank=True, null=True)
    text = models.CharField(max_length=255, verbose_name='Произвольный текст для видом и объемов работ', blank=True)
    date_search = models.DateTimeField(auto_now_add=True)
    scope_work_and_type = models.ForeignKey(TypeService, on_delete=models.CASCADE, blank=True, null=True)

