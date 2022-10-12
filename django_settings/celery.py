# import os

# from celery import Celery


# os.environ.setdefault('DJANGO_SETTING_MODULE', 'django_settings.settings')

# app = Celery('django_settings') # name of cellery service
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request}")




import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_settings.settings")
app = Celery("django_settings")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()