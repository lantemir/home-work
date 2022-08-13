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

