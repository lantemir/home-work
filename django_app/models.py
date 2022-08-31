from statistics import mode

from turtle import title
from unicodedata import category
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


class IcecreamCategory(models.Model):
    title = models.CharField(
        unique=False,
        editable=True,
        blank=True,
        verbose_name="категория морож",
        max_length=250,
    )

    class Meta:
        app_label = 'django_app'
        verbose_name = 'Категория'    
        verbose_name_plural = 'Категории морож'

    def __str__(self) -> str:
        return f'{self.title}'


class Icecream(models.Model):
    title = models.CharField(
        unique=False,
        editable=True,
        blank=True,
        verbose_name="морож",
        max_length=250,
    )

    description = models.TextField(        
        unique=False,
        editable=True,
        blank=True, #можно оставить пустым       
        default="Описание",
        verbose_name="Описание",        
    )

    category_id = models.ManyToManyField(
        blank=True,  
        verbose_name="Категория мороженого",
        to=IcecreamCategory,
    )

class CommentForIcecream(models.Model):
    comment_text = models.TextField(        
        unique=False,
        editable=True,
        blank=True, #можно оставить пустым       
        default="Комментарии",
        verbose_name="комментарии",        
    )

    datetime_field = models.DateTimeField(       
        auto_now_add=True,
        blank=True,
    )

    icecream_id = models.ForeignKey(
        blank=True,
        to=Icecream,
        on_delete=models.CASCADE,
    )

    class Meta:
        app_label = 'django_app' # для отображения в админке и ещё надо изменить и добавить в apps.py
      #  ordering = ('story') # сортировка сначала по title потом по dexcription
        verbose_name = 'Комментарий к истории'    
        verbose_name_plural = 'комментарии к историям'

    def __str__(self) -> str:
        return f'{self.comment_text[:50:1]}' 


class LikeforIcecream(models.Model):
    
    user_id = models.ForeignKey(
        blank=True,
        to=User,
        on_delete=models.CASCADE
    )

    icecream_id = models.ForeignKey(
        blank=True,
        to=Icecream,
        on_delete=models.CASCADE
    )
