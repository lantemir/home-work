
from statistics import mode
from tabnanny import verbose

# from turtle import title
from unicodedata import category
from django.utils import timezone
from django.contrib.auth.models import User, AnonymousUser
from django.db import models
from django.db.models import SET


# расширение user через class


from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.base_user import BaseUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver 

#переопределим юзера 
from django.contrib.auth.models import AbstractBaseUser



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



class Profile(models.Model):
    user = models.OneToOneField(
        primary_key=True,
        editable=True,
        blank=True,
        null=False,
        default=None,
        verbose_name='Аккаунт',

        to=User,
        on_delete=models.CASCADE,
    )

    email = models.EmailField(
        unique=False,
        editable=True,
        blank=True,        
        verbose_name="имэйл: ",
    )

    class Meta:
        app_label = 'auth'
        ordering =('user',)
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
    
    def __str__(self):
        return f'профиль: {self.user.username}'




#сигнал при создании юзера автоматом создаст таблицу profile 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # тут происходит первое создание модели
        Profile.objects.get_or_create(user=instance)
    else:
        Profile.objects.get_or_create(user=instance)




class Task(models.Model):
    # author_id
    author = models.ForeignKey(
        verbose_name='автор',
        to = User,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        unique=False,
        editable=True,
        blank=True,
        verbose_name="задание",
        max_length=250,
    )

    description = models.TextField(
        unique=False,
        editable=True,
        blank=True, #можно оставить пустым       
        default="Описание",
        verbose_name="Описание",  
    )

    datetime_task = models.DateTimeField(       
        auto_now_add=True,
        blank=True,
    )


    class Meta:
        app_label = 'django_app' # для отображения в админке и ещё надо изменить и добавить в apps.py
      #  ordering = ('story') # сортировка сначала по title потом по dexcription
        verbose_name = 'задачи'    
        verbose_name_plural = 'задача'

    def __str__(self) -> str:
        return f'{self.description[:50:1]} {self.title} {self.author.username}' 


class Message(models.Model):
    """
    Model for storing the message of the chat
    """
    sender_user = models.ForeignKey(User, related_name='sender', on_delete=SET(AnonymousUser.id))
    receiver_user = models.ForeignKey(User, related_name='receiver', on_delete=SET(AnonymousUser.id))
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    """
    model for chat rooms
    """
    sender_user = models.ForeignKey(User, related_name='room_sender', on_delete=SET(AnonymousUser.id))
    receiver_user = models.ForeignKey(User, related_name='room_receiver', on_delete=SET(AnonymousUser.id))
    room_name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.room_name




# изменение юзера что бы поменять на имэил вместо логина

class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



# переопределение через класс юзер

# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)




# class UserExtend(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField('email address', unique=True)
#     first_name = models.CharField('first name', max_length=30, blank=True)
#     last_name = models.CharField('last name', max_length=30, blank=True)
#     date_joined = models.DateTimeField('date joined', auto_now_add=True)
    
#     is_active = models.BooleanField('active', default=True)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

#     is_staff = models.BooleanField('if user is moderator', default=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         app_label = 'auth'
#         ordering = ('-date_joined',)
#         verbose_name = 'user'
#         verbose_name_plural = 'users'

#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name

 