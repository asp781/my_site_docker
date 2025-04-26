from django.urls import path
from . import views

urlpatterns = [
    path('estimates/', views.EstimateListCreate.as_view(), name='estimate-list-create'),
    path('estimates/<int:pk>/', views.EstimateRetrieveUpdateDestroy.as_view(), name='estimate-retrieve-update-destroy'),
    path('purchased/', views.PurchasedListCreate.as_view(), name='purchased-list-create'),
    path('purchased/<int:pk>/', views.PurchasedRetrieveUpdateDestroy.as_view(), name='purchased-retrieve-update-destroy'),
    path('completed/', views.CompletedListCreate.as_view(), name='completed-list-create'),
    path('completed/<int:pk>/', views.CompletedRetrieveUpdateDestroy.as_view(), name='completed-retrieve-update-destroy'),
    path('paid/', views.PaidListCreate.as_view(), name='paid-list-create'),
    path('paid/<int:pk>/', views.PaidRetrieveUpdateDestroy.as_view(), name='paid-retrieve-update-destroy'),

    path('login/', views.LoginView.as_view(), name='login'),
]

# https://ekranstroy.ru/api/v1/estimates/ (список смет и создание новых)
# https://ekranstroy.ru/api/v1/estimates/1/ (получение, изменение, удаление сметы с id=1)
# https://ekranstroy.ru/api/v1/purchased/ (список записей о покупке и создание новых)
# https://ekranstroy.ru/api/v1/purchased/1/ (получение, изменение, удаление записи о покупке с id=1)
