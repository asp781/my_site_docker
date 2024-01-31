from django.urls import path

from .views import *

app_name = 'online_registration'

urlpatterns = [
    path('', first_page, name='main_page'),
    path('thanks/', thanks_page, name='thanks_page'),
]
