from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.appointment_id = self.scope['url_route']['kwargs']['appointment_id']
        self.role = self.scope['url_route']['kwargs']['role']
        self.room_group_name = f"chat_{self.appointment_id}_{self.role}"

        # پیوستن به گروه خاص (بر اساس نقش)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # ترک گروه
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # دریافت پیام از WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_id = text_data_json['sender_id']
        role = text_data_json['role']

        # ارسال پیام به گروه خاص (برای کاربر و مشاور)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': sender_id,
                'role': role
            }
        )

    # دریافت پیام از گروه
    async def chat_message(self, event):
        message = event['message']
        sender_id = event['sender_id']
        role = event['role']

        # ارسال پیام به WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender_id': sender_id,
            'role': role
        }))
