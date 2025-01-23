import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatMessage
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        #join the chat room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept() #accept the web socket connection


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        try:
            data = json.loads(text_data)  #handles the incoming message
            message = data['message']
            sender = self.scope['user']   #retrieves sender user
            receiver_id = data['receiver_id']

            # Save message to database
            timestamp = timezone.now()
            await self.save_message(sender.id, receiver_id, message, timestamp)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': sender.username,
                    'timestamp': timestamp.isoformat(),  # Send timestamp as ISO format string
                }
            )

        except KeyError as e:
            print(f"KeyError: {e} - Invalid message format")
        except Exception as e:
            print(f"Error processing message: {e}")

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        timestamp = event['timestamp']

        #send message to web socket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'timestamp': timestamp,
        }))

    @database_sync_to_async
    def save_message(self, sender_id, receiver_id, message, timestamp):  #save message to the database
        try:
            sender = User.objects.get(id=sender_id)
            receiver = User.objects.get(id=receiver_id)
            ChatMessage.objects.create(
                sender=sender,
                receiver=receiver,
                message=message,
                timestamp=timestamp
            )
        except ObjectDoesNotExist:
            print("Error: Sender or receiver does not exist.")
        except Exception as e:
            print(f"Error saving message to database: {e}")