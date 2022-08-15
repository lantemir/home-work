from django.contrib import admin

# Register your models here.
from django_app import models

admin.site.site_header = 'Панель 1'
admin.site.index_title = 'Панель 2'
admin.site.site_title = 'Панель 3'

class TextModelAdmin(admin.ModelAdmin):
    """TextModel"""

    list_display = (
        'author',
        'text',
        'created_datetime',
    )

    list_display_links = (
        'author',    
        'created_datetime',
    )

    list_editable = (
        'text',
    )

    list_filter = (
        'author',
        'text',
        'created_datetime',
    )

    fieldsets = (
        (
            'Основное', {
                "fields": (
                   'author',
                   'text',
                   'created_datetime',
                )
            }
        ),
    )

    search_fields = [
        'author',
        'text',
        'created_datetime',
    ]



class WeatherModelAdmin(admin.ModelAdmin):
    """WeatherMode"""

    list_display = (
        'city_name',
        'city_url',
        'weather_info',
    )

    list_display_links = (
        'city_name',     
    )

    list_editable = (        
        'city_url',
    )

    list_filter = (
        'city_name',
        'city_url',
        'weather_info',      
    )

    fieldsets = (
        (
            'Основное', {
                "fields": (
                   'city_name',
                   'city_url',
                   'weather_info',                     
                )
            }
        ),
    )

    search_fields = [
        'city_name',
        'city_url',
        'weather_info',        
    ]




admin.site.register(models.WeatherModel, WeatherModelAdmin)
admin.site.register(models.TextModel, TextModelAdmin)