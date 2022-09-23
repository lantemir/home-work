# from cgitb import html
import os
from distutils.log import error
from multiprocessing import context
import re
from sqlite3 import Timestamp

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django_app import models
from django.core.paginator import Paginator
from django_app import serializers

from django.contrib.auth.models import User, update_last_login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.crypto import get_random_string

from django_app.models import Room, Message




from django.core.mail import send_mail # для отправки писем
import requests
from bs4 import BeautifulSoup


# для классов
from django.views import View
from rest_framework.views import APIView


#чат
from . forms import SignUpForm 
from django.contrib.auth import login

#Email
import smtplib
from email.mime.text import MIMEText

# Create your views here.

def index(request):
    context={}
    return render(request=request, template_name = 'build/index.html', context=context, status=status.HTTP_200_OK)

def users(request):
    return JsonResponse({"response": "Ok!"})

@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
def chat(request, sms_id = None):
    try:
        if sms_id:
            if request.method == "GET":
                return Response(status=status.HTTP_200_OK)
            elif request.method == "PUT" or request.method == "PATCH":
                return Response(status=status.HTTP_200_OK)
            elif request.method == "DELETE":
                return Response(status=status.HTTP_200_OK)
            else: 
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            if request.method == "GET":
                page = int(request.GET.get("page", 1))
                limit = int(request.GET.get("limit", 3))

                obj_list = models.TextModel.objects.all()
                paginator_obj = Paginator(object_list= obj_list, per_page=limit)
                curent_page = paginator_obj.get_page(page).object_list
                serialized_obj_list = serializers.TextModelSerializer(instance=curent_page, many=True).data

                return Response(data={"list": serialized_obj_list, "x-total-count": len(obj_list)}, status=status.HTTP_200_OK)

            elif request.method == "POST":
                text = int(request.GET.get("text", ""))
                if text:
                    models.TextModel.objects.create(
                        text=text
                    )
                    return Response(status=status.HTTP_201_CREATED)           
                return Response(status=status.HTTP_204_NO_CONTENT)
            else: 
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as error:
        print(error)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
def weather(request, weather_id = None):
    try:
        if weather_id:        
            if request.method == "GET":  
                city_by_id = models.WeatherModel.objects.get(pk = weather_id)              

                serialized_weather_by_id = serializers.WeatherModelSerializer(instance=city_by_id, many=False).data

                url = serialized_weather_by_id["city_url"]

                city = serialized_weather_by_id["city_name"]

                headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

                response = requests.get(url=url, headers=headers)

                soup = BeautifulSoup(response.content, 'html.parser')

             
                data1 = soup.find_all("span", attrs={"class": "unit unit_temperature_c"})[0]

                

                sign = str(data1).split('sign">')[1].split('</span>')[0].strip()

                temp = str(data1).split('</span>')[1].split('<span')[0].strip()               

                print("data1: ")
                print(data1)

                print("sign: ")
                print(sign)

                print("temp: ")
                print(temp)



                return Response( {"sign": sign, "temp": temp, "city":city, "status": status.HTTP_200_OK})

        else: 
            if request.method == "GET":             
                obj_list = models.WeatherModel.objects.all()
                serialized_obj_list = serializers.WeatherModelSerializer(instance=obj_list, many=True).data

                return Response(data={"list": serialized_obj_list, "x-total-count": len(obj_list)}, status=status.HTTP_200_OK)        

            
    except Exception as error:
        print(error)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(http_method_names=["GET", "POST"])
def icecream(request, icecream_id=None):
    try:
        if icecream_id:
            if request.method == "GET":  

                # print("icecream_id:  ")
                # print(icecream_id)
                
                currentPage = int(request.GET.get("currentPage", 1))
                pageSize = int(request.GET.get("pageSize", 4))
                iceCreamInfo = models.Icecream.objects.get(id = icecream_id )
                icecream_obj = serializers.IceCreamModelSerializer(instance=iceCreamInfo, many=False).data

                # print('icecream_obj: ')
                # print(icecream_obj)

                count = models.CommentForIcecream.objects.filter(icecream_id = icecream_id).count()
                commentget = models.CommentForIcecream.objects.filter(icecream_id = int(icecream_id))
                
               

                # print('obj_list: ')
                # print(obj_list)

                comment_serialized_obj_list = serializers.CommentForIcecreamModelSerializer(instance=commentget, many=True).data


                # print('serialized_obj_list: ')
                # print(serialized_obj_list)


                paginator_obj = Paginator(comment_serialized_obj_list, pageSize)
                current_page_comment = paginator_obj.get_page(currentPage).object_list

                return Response(data={ "x_total_count_comment": count, "icecream_obj":icecream_obj, "comment":current_page_comment }, status=status.HTTP_200_OK)


        else: 
            if request.method == "GET":  

                currentPage = int(request.GET.get("currentPage", 1))
                pageSize = int(request.GET.get("pageSize", 4))

                obj_list = models.Icecream.objects.all()           
                serialized_obj_list = serializers.IceCreamModelSerializer(instance=obj_list, many=True).data

                paginator_obj = Paginator(serialized_obj_list, pageSize)

                currentPage = paginator_obj.get_page(currentPage).object_list


                return Response(data={"list": currentPage, "x_total_count": len(obj_list) }, status=status.HTTP_200_OK)        

            
    except Exception as error:
        print(error)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)





#парсинг
# https://www.youtube.com/watch?v=kZ8f6PqW65o&list=PLFH0jFGRecS0btzEqlp6f4Ua8FwJYkH1m&index=32&t=10499s
# https://github.com/bogdandrienko/PyE-212-2/blob/main/projects/3/app_teacher/parser_html_data.py

@api_view(http_method_names=["GET", "POST"])
def comment_icecream(request, icecream_id=None):
    try:
        if icecream_id:
            if request.method == "GET":  

                print("icecream_id:  ")
                print(icecream_id)
                
                currentPage = int(request.GET.get("currentPage", 1))
                pageSize = int(request.GET.get("pageSize", 4))

                count = models.CommentForIcecream.objects.all()
                obj_list = models.CommentForIcecream.objects.filter(icecream_id = int(icecream_id))

                serialized_obj_list = serializers.CommentForIcecreamModelSerializer(instance=obj_list, many=True).data


                print("serialized_obj_list:  ")
                print(serialized_obj_list)

                paginator_obj = Paginator(serialized_obj_list, pageSize)
                current_page = paginator_obj.get_page(currentPage).object_list

                return Response(data={"list": current_page, "x_total_count": count}, status=status.HTTP_200_OK)


        else: 
            pass 
            # if request.method == "GET":  

            #     currentPage = int(request.GET.get("currentPage", 1))
            #     pageSize = int(request.GET.get("pageSize", 4))

            #     obj_list = models.CommentForIcecream.objects.all()
            #     serialized_obj_list = serializers.CommentForIcecreamModelSerializer(instance=obj_list, many=True).data

            #     paginator_obj = Paginator(serialized_obj_list, pageSize)
            #     current_page = paginator_obj.get_page(currentPage).object_list

            #     return Response(data={"list": current_page, "x_total_count": len(obj_list) }, status=status.HTTP_200_OK)

    except Exception as error:
        print(error)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(http_method_names=["GET", "POST"])
def sendingemail(request):
    try:
        if request.method == "POST":

            password = os.getenv("EMAIL_PASSWORD")       

            localemail = "emailsenderinform@gmail.com"

            sender = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            try:
                server.login(localemail, password)
                msg =  MIMEText(message)
                msg["Subject"] = subject
               

                server.sendmail(localemail, sender, msg.as_string())
                # server.sendmail(sender, 'temiros@mail.ru', f"Subject: {sbj.as_string()}\n{msg.as_string()}")

                return Response(status=status.HTTP_200_OK)

                

            except Exception as _ex:
                return Response( data={"result":  f"{_ex}\nCheck login or password please"}, status=status.HTTP_400_BAD_REQUEST )


            

           
    
    except Exception as error:
        return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(http_method_names=["GET", "POST"])
def jsonplaceholder(request):
    try:
        
        if request.method == "POST":  

            sendMessage = request.POST.get("sendMessage", "")
            

            print("sendMessage:  ")
            print(sendMessage)


            return Response(data={"result": sendMessage}, status=status.HTTP_200_OK)




    except Exception as error:
        print(error)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def registration(request):
    if request.method == "POST":
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        print(f"\nGET {request.GET}")
        print(f"POST {request.POST}")
        print(f"data {request.data}")
        print(f"FILES {request.FILES}\n")

        print(email)
        print(password)

        if email and password:
            if re.match(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password) and \
                    re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email):
                User.objects.create_user(
                    username=email,
                    email=email,
                    password=password
                )

                # {
                #     "email": "admin@gmail.com",
                #     "password": "adminA1#"
                # }
                pass
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(data={"ответ:": "Вы не прошли проверку регулярного выражения"}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)




class Mylist(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        obj_list = models.Task.objects.all()
        serialized_obj_list = serializers.TaskModelSerializer(instance=obj_list, many=True).data

        obj_users = User.objects.all()
        serialized_obj_users = serializers.UserModelSerializer(instance=obj_users, many=True).data

        # currentPage = int(request.GET.get("currentPage", 1))
        # pageSize = int(request.GET.get("pageSize", 4))

        # obj_list = models.Icecream.objects.all()           
        # serialized_obj_list = serializers.IceCreamModelSerializer(instance=obj_list, many=True).data

        # paginator_obj = Paginator(serialized_obj_list, pageSize)

        # currentPage = paginator_obj.get_page(currentPage).object_list



        content = {
            'status': 'request GET', 
            'data': serialized_obj_list,
            'users': serialized_obj_users,
        }

        return Response(content)


    

    def post(self, request, format=None):      

        entry_selectedUserId = int(request.data.get("selectedUserId"))
        entry_title = request.data.get("title")
        entry_description = request.data.get("description")

        if(entry_selectedUserId > 0):        
            models.Task.objects.create(
                author_id = entry_selectedUserId,
                title = entry_title,
                description = entry_description,
            )  

            obj_list = models.Task.objects.all()
            serialized_obj_list = serializers.TaskModelSerializer(instance=obj_list, many=True).data     

            content = {
                'data': serialized_obj_list,
                'status': status.HTTP_201_CREATED
            }
            return Response(content)
        
        else:
            content = {
                'response': 'Не выбрали автора',
                'status': status.HTTP_400_BAD_REQUEST
            }
            return Response(content)
        
    
    def delete(self, request, item_id = 0):
       
        task_id = item_id      
       

        models.Task.objects.get(id = task_id).delete()

        obj_list = models.Task.objects.all()
        serialized_obj_list = serializers.TaskModelSerializer(instance=obj_list, many=True).data
        


        content = {
            'data': serialized_obj_list,
            'status': status.HTTP_200_OK
        }
        return Response(content)



    def put(self, request ):
       

        task_id = request.data.get("objIdForUpdate")
        entry_selectedUserId = int(request.data.get("selectedUserId"))
        entry_title = request.data.get("title")
        entry_description = request.data.get("description")

        task = models.Task.objects.get(id = task_id)

        if task.title != entry_title:
                task.title = entry_title

        task.description = entry_description
        task.author = User.objects.get(pk = entry_selectedUserId)
           
        task.save()



        obj_list = models.Task.objects.all()
        serialized_obj_list = serializers.TaskModelSerializer(instance=obj_list, many=True).data     

        content = {
            'data': serialized_obj_list,
            'status': status.HTTP_201_CREATED
        }
        return Response(content)




# чат 
# class GetAllUsers(LoginRequiredMixin, View):
#     def get(self, request):
        
#         #to get list of all users from the database
        
#         print(request.user)
#         users = User.objects.all()        

#         content = {
#             'status': status.HTTP_200_OK,             
#             'users': users,
#         }
#         return Response(content)

#     def post (self, request):

#         # to get the sender and receiver users and connect them with their respective room

#         sender = request.user.id
#         receiver = request.POST['users']

#         sender_user = User.objects.get(id = sender)
#         receiver_user = User.objects.get(id = receiver)
#         # settings the receiver as a session variable
#         request.session['receiver_user'] = receiver

#         #check if the sender and receiver already have a room
#         get_room = Room.objects.filter(Q(sender_user=sender_user,
#         receiver_user=receiver_user) | Q(sender_user=receiver_user, 
#         receiver_user=sender_user))

#         #fetch the room name if room already exist
#         if get_room:
#             room_name = get_room[0].room_name
        
#         #create a new room if room doesn't exist
#         else:
#             new_room = get_random_string(10)

#             while True:
#                 room_exist = Room.objects.filter(room_name=new_room)
#                 if room_exist:
#                     new_room = get_random_string(10)
#                 else:
#                     break
#             create_room = Room.objects.create(sender_user=sender_user,
#             receiver_user=receiver_user, room_name=new_room)
#             create_room.save()
#             room_name = create_room.room_name
#         return redirect('room', room_nam=room_name)


# class ChatRoom(LoginRequiredMixin, View):
#     queryset = Room.objects.all()

#     def get(self, request, room_name, *args, **kwargs):
#         get_object_or_404(Room, room_name=self.kwargs.get("room_name"))
#         room = Room.objects.get(room_name=self.kwargs.get("room_name"))
#         sender = request.user.id
#         sender_name = User.objects.get(id=sender).username

#         # sets up the user  as sender user for chatting
#         if room.receiver_user.id == sender:
#             receiver = room.sender_user.id
#         else:
#             receiver = room.receiver_user.id

#         # get all the previous messages from the database
#         messages = Message.objects.filter(Q(sender_user=sender, 
#         receiver_user = receiver) | Q(sender_user=receiver, 
#         receiver_user = sender)).order_by('timestamp')

        
#         content = {
#             'status': status.HTTP_200_OK,             
#             'room_name': room_name,
#             'sender_id': sender,
#             'receiver_id': receiver,
#             'messages': messages,
#             'sender_name': sender_name
#         }
#         return Response(content)






def frontpage(request):
    return render(request, 'django_app/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    
    else:
        form = SignUpForm()
    
    return render(request, 'django_app/signup.html', {'form': form})