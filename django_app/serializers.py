from asyncore import read
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django_app import models
from django.contrib.auth.models import User



class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ['id', 'username', 'email']


class TextModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextModel
        fields = "__all__"


class WeatherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeatherModel
        fields = "__all__"



# class IcecreamCategoryModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.IcecreamCategory
#         fields = "__all__"


class CommentForIcecreamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentForIcecream
        fields = "__all__"



class IcecreamCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IcecreamCategory
        fields = "__all__"




class IceCreamModelSerializer(serializers.ModelSerializer):
    category_id = serializers.SerializerMethodField(read_only=True)

    comments = serializers.SerializerMethodField(read_only=True)

    likes = serializers.SerializerMethodField(read_only= True)

    class Meta:
        model = models.Icecream
        fields = "__all__"

    def get_category_id(self, obj): # obj  models.Icecream

        list1 = []

        for obj in obj.category_id.all():
            serialized_obj_list = IcecreamCategoryModelSerializer(instance=obj, many=False).data
            list1.append(serialized_obj_list)
        
        return list1    

       # return str(obj) + "проверка"

    def get_comments(self, obj):

        # return {"apples": "1234124124"}
       # return CommentForIcecreamModelSerializer(instance=obj.id, many=True).data
       #return models.CommentForIcecream.objects.get(id = obj.id)
    #    return models.CommentForIcecream.objects.get()

        obj_list = models.CommentForIcecream.objects.filter(icecream_id = obj.id)
        return CommentForIcecreamModelSerializer(instance=obj_list, many=True).data[:3]

    def get_likes(self, obj):

        likeCount = models.LikeforIcecream.objects.filter(icecream_id = obj.id).count()

        return {"likeCount": likeCount}



class TaskModelSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField(read_only = True)
    all_users = serializers.SerializerMethodField(read_only = True)
    

    class Meta:
        model = models.Task
        fields = "__all__"

    def get_users(self, obj):

     
        obj_list = User.objects.filter(id=obj.author_id)
        # obj_list = User.objects.all()

        return UserModelSerializer(instance=obj_list, many=True).data

    def get_all_users(self, obj):

        obj_list = User.objects.all()

        return UserModelSerializer(instance=obj_list, many=True).data



# https://docs.djangoproject.com/en/4.1/topics/db/queries/

  

       

    




        

        

