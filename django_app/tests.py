
from urllib import response
from django.contrib.auth.models import User
from django.test import TestCase, Client 
from django.urls import reverse
from rest_framework import status

from django_app import models, serializers, views



class MyTestException(Exception):
    def __init__(self, error_message:str):
        self.error_message = error_message

        def error(self):
            return f"{self.error_message} |"

class CustomTest:
    @staticmethod
    def run_test():
        try:
            print('test BEGIN')
            title_1 = models.IcecreamCategory.objects.create(title='title 1')
            title_2 = models.IcecreamCategory.objects.create(title='title 2')

            if title_1.test_get_title() != f'title 1':
                raise MyTestException('проверка 1 не пройдена')
            if title_2.test_get_title() != f'2 title 2':
                raise MyTestException('проверка 2 не пройдена')

            
        except MyTestException as error:
            print (f'run_test MyTestException fail: {error}')

        except Exception as error:
            print (f'run_test fail: {error}')

        else: 
            print('run_test OK')
        finally:
            print('test END')



# class CustomTestJWTtoken:
#     @staticmethod
#     def run_test():
#         try:
#             print('test BEGIN')
         
#             import requests

#             headers = {"user-agent": "user"}
#             response = requests.post(
#                 url="http://127.0.0.1:8000/api/token/",
#                 headers=headers,
#                 data={
#                     "username": "temir",
#                     "password": "temir"
#                 }
#             )

            

            
#         except MyTestException as error:
#             print (f'run_test MyTestException fail: {error}')

#         except Exception as error:
#             print (f'run_test fail: {error}')

#         else: 
#             print('run_test OK')
#             print(response) 
#         finally:
#             print('test END')


# CustomTest.run_test()

# CustomTestJWTtoken.run_test()

class IcecreamCategoryModelTestCase(TestCase):
     
    def setUp(self) -> None:
        # models.IcecreamCategory.objects.create(title='title 1')
        # models.IcecreamCategory.objects.create(title='title 2')

        #CustomTest.run_test()

        # CustomTestJWTtoken.run_test()
        pass


    def test_title(self):
        pass
        # title_1 = models.IcecreamCategory.objects.get(title="title 1")
        # title_2 = models.IcecreamCategory.objects.get(title="title 2")
        # self.assertEqual(title_1.test_get_title(), f'title 1')
        # self.assertEqual(title_2.test_get_title(), f'title 2')

    def test_token(self):
        import requests

        try:

            headers = {"user-agent": "user"}
            response = requests.post(
                url="http://127.0.0.1:8000/api/token/",
                headers=headers,
                data={
                    "username": "temir",
                    "password": "temir"
                }
            )


        except MyTestException as error:
            print (f'run_test MyTestException fail: {error}')

        except Exception as error:
            print (f'run_test fail: {error}')

        else: 
            print('run_test OK')
            status = response.status_code

            self.assertEqual(status, 200)

            print(response) 
        finally:
            print('test END')


        

        # status = response.status_code

        # self.assertEqual(status, 200)


# if __name__ == "__main__":
#     # CustomTest.run_test()

# if __name__ == "__main__":
#     CustomTestJWTtoken.run_test()

