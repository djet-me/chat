import json
from asgiref.sync import async_to_sync

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('general', self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)('general', self.channel_name)

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({'message': message}))
