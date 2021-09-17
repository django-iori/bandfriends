import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room_name = text_data_json['room_name']
        self_name = text_data_json['self_name']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'room_name': room_name,
                'self_name': self_name
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        room_name = event['room_name']
        self_name = event['self_name']
        #メッセージの保存
        message_db = Message()
        room = Room.objects.get(name=room_name)
        message_db.content = message
        message_db.name = self_name
        message_db.room = room
        message_db.save()
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'self_name': self_name
        }))
