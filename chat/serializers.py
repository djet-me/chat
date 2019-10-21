from rest_framework import serializers

from chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'user', 'timestamp', 'text']

    def create(self, validated_data):
        user = self.context['request'].user
        message = Message(user=user, text=validated_data['text'])
        message.save()
        return message

    # noinspection PyMethodMayBeStatic
    def get_timestamp(self, instance):
        return f'{instance.date_created.time().hour}:{str(instance.date_created.time().minute).rjust(2, "0")}'

    # noinspection PyMethodMayBeStatic
    def get_user(self, instance):
        return instance.user.username
