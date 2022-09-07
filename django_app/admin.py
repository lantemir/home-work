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



class IcecreamModelAdmin(admin.ModelAdmin):
    """IcecreamModel"""

    list_display = (
        'title',
        'description', 
        
     
    )
    filter_horizontal = ('category_id',) # только для полей флрмата many to many fields

    list_display_links = (
        'title',     
    )

    list_editable = (        
        'description',       
    )

    list_filter = (
        'title',
        'description',       
    )

    fieldsets = (
        (
            'Основное', {
                "fields": (
                   'title',
                   'description',   
                   'category_id',               
                )
            }
        ),
    )

    search_fields = [
        'title',
        'description',          
    ]


class IcecreamCategoryModelAdmin(admin.ModelAdmin):
    """IcecreamCategoryModel"""

    list_display = (
        'title', 
    )

    list_display_links = (
         
    )


    list_filter = (
         
    )

    fieldsets = (
        (
            'Основное', {
                "fields": (
                   'title',                               
                )
            }
        ),
    )



class CommentModelAdmin(admin.ModelAdmin):
    """CommentModel"""

    list_display = (
        'comment_text',
        'datetime_field',
        'icecream_id',
    )

    list_display_links = (
          
    )

    list_editable = (        
        
    )

    list_filter = (
        'datetime_field',         
    )

    fieldsets = (
        (
            'Основное', {
                "fields": (
                   'comment_text',                  
                   'icecream_id',                     
                )
            }
        ),
    )

    search_fields = [
        'comment_text',             
    ]


class LikeModelAdmin(admin.ModelAdmin):
    """LikeModel"""

    list_display = (
        'user_id',
        'icecream_id',        
    )

    list_display_links = (
          
    )

    list_editable = (        
        
    )

    list_filter = (
              
    )

    fieldsets = (
        (
            'Основное', {
                "fields": (
                   'user_id',
                   'icecream_id',                     
                )
            }
        ),
    )

    search_fields = [
                  
    ]



class TaskModelAdmin(admin.ModelAdmin):
    """TaskModel"""

    list_display = (
        'title',
        'description',  
        'author',  
        'datetime_task',      
    )

    list_display_links = (
          
    )

    list_editable = (        
        'description',
    )

    list_filter = (
        'author', 
        'datetime_task',   
    )

    fieldsets = (
        (
            'Основное', {
                "fields": (
                   'title',
                   'description',  
                   'author',   
                   
                                           
                )
            }
        ),
    )

    search_fields = [
                  
    ]



   




admin.site.register(models.WeatherModel, WeatherModelAdmin)
admin.site.register(models.TextModel, TextModelAdmin)
admin.site.register(models.Icecream, IcecreamModelAdmin)
admin.site.register(models.IcecreamCategory, IcecreamCategoryModelAdmin)
admin.site.register(models.CommentForIcecream, CommentModelAdmin)

admin.site.register(models.LikeforIcecream, LikeModelAdmin)

admin.site.register(models.Profile)
admin.site.register(models.Task, TaskModelAdmin)
# admin.site.register(models.UserExtend)

