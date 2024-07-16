from django.urls import path

from .views import *


app_name = 'app4'

urlpatterns = [
    path('', index, name='index_4'),
    path('delete_record/<int:pk>', delete_record, name='delete_record'),
    path('edit_record/<int:pk>', RecordUpdate.as_view(), name='edit_record'),
    ]
