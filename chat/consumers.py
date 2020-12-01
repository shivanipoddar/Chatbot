import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Booking
import datetime


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
        try :
            text_data_json['task']
            global cid
            try:
                Booking.objects.filter(id=cid).update(restype = text_data_json['task'])
            except:
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'task': text_data_json['task']
                    }
                )
                ty = Booking(restype = text_data_json['task'])
                # ty.save()
                cid = ty.id
        except:
            try:
                text_data_json['per']
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'per': text_data_json['per']
                    }
                )
                Booking.objects.filter(id=cid).update(tperson=text_data_json['per'])
            except:
                try:
                    text_data_json['date']
                    now = datetime.datetime.now()
                    async_to_sync(self.channel_layer.group_send)(
                        self.room_group_name,
                        {
                            'type': 'chat_message',
                            'date': text_data_json['date']
                        }
                    )
                    Booking.objects.filter(id=cid).update(date=now)
                except :
                    try:
                        text_data_json['name']
                        async_to_sync(self.channel_layer.group_send)(
                            self.room_group_name,
                            {
                                'type': 'chat_message',
                                'name': text_data_json['name']
                            }
                        )
                        Booking.objects.filter(id=cid).update(name=text_data_json['name'])
                    except:
                        try:
                            text_data_json['contact']
                            async_to_sync(self.channel_layer.group_send)(
                                self.room_group_name,
                                {
                                    'type': 'chat_message',
                                    'contact': text_data_json['contact']
                                }
                            )
                            Booking.objects.filter(id=cid).update(contact=text_data_json['contact'])
                        except:
                            pass


    # Receive message from room group
    def chat_message(self, event):
        try:
            event['task']
            message = event['task']
        except:
            try :
                event['per']
                message = event['per']
            except:
                try:
                    event['date']
                    message = event['date']
                except:
                    try:
                        event['name']
                        message = event['name']
                    except:
                        try:
                            event['contact']
                            message = event['contact']
                        except:
                            pass


        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))