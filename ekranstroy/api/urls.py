from django.urls import path

from .views import *

urlpatterns = [
    path('cat/', cat_list, name='cat'),
    path('order/', order_list, name='order'),
    ]

# http://127.0.0.1:8000/api/v1/cat
# http://127.0.0.1:8000/api/v1/order
