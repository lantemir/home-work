# Generated by Django 4.1 on 2022-09-18 15:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_app', '0007_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=200, unique=True)),
                ('receiver_user', models.ForeignKey(on_delete=models.SET(None), related_name='room_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender_user', models.ForeignKey(on_delete=models.SET(None), related_name='room_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('receiver_user', models.ForeignKey(on_delete=models.SET(None), related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender_user', models.ForeignKey(on_delete=models.SET(None), related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
