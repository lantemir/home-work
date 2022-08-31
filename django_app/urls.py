

from django.urls import path, re_path
from django_app import views


urlpatterns = [
    path('', views.index, name="index"),

    re_path(route=r'^users/$', view=views.users, name="users"),

    re_path(route=r'^chat/(?P<sms_id>\d+)/$', view=views.chat, name="chat_id"),
    re_path(route=r'^chat/$', view=views.chat, name="chat"),

    re_path(route=r'^weather/$', view=views.weather, name="weather"),
    re_path(route=r'^weather/(?P<weather_id>\d+)/$', view=views.weather, name="weather_id"),

    re_path(route=r'^icecream/(?P<icecream_id>\d+)/$', view=views.icecream, ),
    re_path(route=r'^icecream/$', view=views.icecream, ),
    

    re_path(route=r'^commenticecream/(?P<icecream_id>\d+)/$', view=views.comment_icecream),

    re_path(route=r'^jsonplaceholder/$', view=views.jsonplaceholder),
]



