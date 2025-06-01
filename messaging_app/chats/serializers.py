from django_rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.Serializer):
    """
    Serializer for User model.
    """
    user_id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    is_active = serializers.BooleanField(default=True)
    is_deleted = serializers.BooleanField(default=False)
    is_archived = serializers.BooleanField(default=False)
    is_muted = serializers.BooleanField(default=False)
    is_pinned = serializers.BooleanField(default=False)
    is_starred = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = '__all__'


class ConversationSerializer(serializers.Serializer):
    """
    Serializer for Conversation model.
    """
    conversation_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    participants = UserSerializer(many=True, required=True)
    is_group = serializers.BooleanField(default=False)
    is_archived = serializers.BooleanField(default=False)
    is_muted = serializers.BooleanField(default=False)
    is_deleted = serializers.BooleanField(default=False)
    is_pinned = serializers.BooleanField(default=False)
    is_starred = serializers.BooleanField(default=False)

    class Meta:
        model = Conversation
        fields = '__all__'


class MessageSerializer(serializers.Serializer):
    """
    Serializer for Message model.
    """
    message_id = serializers.UUIDField(read_only=True)
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())
    sender = UserSerializer(read_only=True)
    content = serializers.CharField(required=True)
    timestamp = serializers.DateTimeField(auto_now_add=True)
    is_read = serializers.BooleanField(default=False)

    class Meta:
        model = Message
        fields = '__all__'
