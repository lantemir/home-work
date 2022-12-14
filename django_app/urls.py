
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django_app import views

from django_app.views import Mylist

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.index, name="index"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    

    re_path(route=r'^users/$', view=views.users, name="users"),

    re_path(route=r'^chat/(?P<sms_id>\d+)/$', view=views.chat, name="chat_id"),
    re_path(route=r'^chat/$', view=views.chat, name="chat"),

    re_path(route=r'^weather/$', view=views.weather, name="weather"),
    re_path(route=r'^weather/(?P<weather_id>\d+)/$', view=views.weather, name="weather_id"),

    re_path(route=r'^icecream/(?P<icecream_id>\d+)/$', view=views.icecream, ),
    re_path(route=r'^icecream/$', view=views.icecream, ),
    

    re_path(route=r'^commenticecream/(?P<icecream_id>\d+)/$', view=views.comment_icecream),

    re_path(route=r'^jsonplaceholder/$', view=views.jsonplaceholder),

    path('registration/', views.registration),

    path('mylistdj/<item_id>/',  Mylist.as_view()),
    path('mylistdj/',  Mylist.as_view()),

    re_path(route=r'^sendemail/$', view=views.sendingemail, name="sendingemail"),

    path('download_img/', view=views.download_img, name='download_img'),

    path('seleryredis/', view=views.seleryredis, name='seleryredis'),


    

    # path('frontpage/', views.frontpage, name='frontpage'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name = 'django_app/login.html'), name='login' ),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path('rooms/', views.GetAllUsers.as_view(), name='rooms'),
    # path('rooms/<str:room_name>/', views.ChatRoom.as_view(), name='room'),
    

    
]


