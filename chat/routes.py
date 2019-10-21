from rest_framework import routers

from chat.views import MessageViewSet


chat_router = routers.SimpleRouter()
chat_router.register('messages', MessageViewSet, 'messages')
