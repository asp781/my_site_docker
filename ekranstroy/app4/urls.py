from django.urls import path

from .views import *


app_name = 'app4'

urlpatterns = [
    path('', index, name='index_4'),
    path('delete_record/<int:pk>', delete_record, name='delete_record'),
    path('edit_record/<int:pk>', RecordUpdate.as_view(), name='edit_record'),

    path('api/v1/records/', RecordListCreate.as_view(), name='record-list-create'),
    path('api/v1/records/<int:pk>/', RecordRetrieveUpdateDestroy.as_view(), name='record-retrieve-update-destroy'),
    ]

# http://ekranstroy.ru/secret/api/v1/records/
# http://ekranstroy.ru/secret/api/v1/records/7
