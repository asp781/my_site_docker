# chat/urls.py
from django.urls import path

from . import views
app_name = 'chat'

urlpatterns = [
    path("<str:room_name>/", views.room, name="room"),
]

# docker run -it --rm --name redis -p 6379:6379 redis
# daphne ekranstroy.asgi:application
# http://127.0.0.1:8000/chat/testroom/
# netstat -ano | findstr :6379
# taskkill /PID <PID> /F
# pip install channels channels-redis redis
# pip install daphne
# pip freeze > requirements.txt
# http://localhost/chat/testroom/
# https://ekranstroy.ru/chat/testroom/
