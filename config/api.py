from django.urls import path, include

from chat.routes import chat_router


api_urls = [
    path('api/v1/messages/', include((chat_router.urls, 'chat_api'), 'chat_api'), name='chat_api'),
]
