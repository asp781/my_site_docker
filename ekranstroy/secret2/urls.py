from django.urls import path

from .views import *


app_name = 'secret2'

urlpatterns = [
    path('<slug:slug>/', index, name='secret2'),
    ]
