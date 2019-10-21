from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication

from chat.models import Message
from chat.serializers import MessageSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = (CsrfExemptSessionAuthentication,)
