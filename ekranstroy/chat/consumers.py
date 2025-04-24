# chat/consumers.py
import json
from pprint import pprint

from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        pprint(self.scope)

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Получаем имя пользователя из scope
        user = self.scope["user"]
        self.username = user.username

        # Добавляем пользователя в группу комнаты
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Удаляем пользователя из группы комнаты
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Получаем сообщение от WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        # text_data_json приходит имя пользователя от Андроид-клиента, от Веб-клиента не приходит
        message = text_data_json["message"]
        
        username = text_data_json.get("username")
        if not username:
            username = self.username

        # Отправляем сообщение в группу комнаты с именем пользователя
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message,
                # "username": self.username,
                "username": username,
            },
        )

    # Получаем сообщение от группы комнаты
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]

        # Отправляем сообщение в WebSocket с именем пользователя
        await self.send(
            text_data=json.dumps(
                {"message": message, "username": username}
            )
        )
