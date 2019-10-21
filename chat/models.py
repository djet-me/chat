from django.db import models
from django.conf import settings
from django.utils import timezone

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f'Message from {self.user}'

    def notify_ws_clients(self):
        notification = {'type': 'chat_message', 'message':
            {
                'id': self.pk,
                'timestamp': f'{timezone.now().time().hour}:{str(timezone.now().time().minute).rjust(2, "0")}',
                'user': self.user.username,
                'text': self.text
            }
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)('general', notification)

    def save(self, *args, **kwargs):
        is_new = not self.pk
        self.text = self.text.strip()
        super().save(args, kwargs)
        if is_new:
            self.notify_ws_clients()

    class Meta:
        app_label = 'chat'
        ordering = ('date_created',)
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
