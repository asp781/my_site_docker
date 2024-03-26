from django.urls import path

from .views import *

urlpatterns = [
    path('cat/', cat_list, name='cat'),
    ]

# https://ekranstroy.ru/api/v1/cat
