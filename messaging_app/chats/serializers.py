from django_rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id', 'username', 'email', 'first_name', 'second_name',
            'last_name', 'phone_number', 'profile_picture', 'created_at',
            'updated_at', 'is_active', 'is_superuser', 'is_online',
            'last_login', 'is_verified', 'is_blocked', 'is_deleted',
            'is_archived', 'is_muted', 'is_pinned', 'is_starred'
        ]


class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for the Conversation model.
    """
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            'conversation_id', 'name', 'participants', 'created_at',
            'updated_at', 'is_group', 'is_archived', 'is_muted',
            'is_deleted', 'is_pinned', 'is_starred', 'is_forwarded',
            'forwarded_from'
        ]


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for the Message model.
    """
    conversation = ConversationSerializer(read_only=True)
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = [
            'message_id', 'conversation', 'sender', 'message_body',
            'timestamp', 'is_read', 'is_deleted', 'is_forwarded',
            'forwarded_from'
        ]