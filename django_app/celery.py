from distutils.log import error
from email import message
import os
from time import time
from celery import shared_task
from django.contrib.auth.models import User

@shared_task
def add(x, y):
    return x + y


@shared_task
def count_users():
    time.sleep(3.0)
    return User.objects.count()    

# парсинг, отправка почты, отчёты, анализы, изображение
# @shared_task
# def send_mass_email(recipients: list, message: dict, skip_error=True):
#     for recipient in recipients:
#         try:
#             #send_email(recipient, message)
#             pass
#         except Exception as error:
#             if skip_error is False:
#                 break 


# os.environ.setdefault('DJANGO_SETTING_MODULE', 'django_settings.settings')

# app = Celery('django_settings')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request}")

