from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class TextModel(models.Model):
    author = models.ForeignKey(
        verbose_name='автор',
        to = User,
        on_delete=models.CASCADE,
    )
    text = models.CharField(
        verbose_name='текст',
        max_length=500,
    )
    created_datetime = models.DateField(
        default=timezone.now,
        verbose_name='время создания'
    )



class WeatherModel(models.Model):
    city_name = models.CharField(
        verbose_name='название города',
        max_length=500,
    )
    city_url = models.TextField(
        verbose_name='ссылка на город',
    )
    weather_info = models.TextField(
        verbose_name='информация по погоде',
        blank=True,
    )


    class Meta:
        app_label = 'django_app' # для отображения в админке и ещё надо изменить и добавить в apps.py
            # ordering = ('title') # сортировка сначала по title потом по dexcription
        verbose_name = 'Погода1'    
        verbose_name_plural = 'Погода2'

        def __str__(self) -> str:
            return f'{self.city_name}'  