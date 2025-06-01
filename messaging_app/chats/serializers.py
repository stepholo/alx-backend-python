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
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_full_name(self, obj: User) -> str:
        """ Returns the full name of the user by combining first and last names."""
        return f"{obj.first_name} {obj.last_name}".strip()

    def validate_email(self, value: str) -> str:
        """ Validates that the email ends with '.com' """
        if not value.endswith('.com'):
            raise serializers.ValidationError("Email must end with .com")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        if not value:
            raise serializers.ValidationError("Email cannot be empty")
        if not value.startswith.upper():
            raise serializers.ValidationError("Email must start with an uppercase letter")
        if not value[0].isalpha():
            raise serializers.ValidationError("Email must start with a letter")
        if value.find('@') == -1:
            raise serializers.ValidationError("Email must contain '@'")
        return value

    def validate_username(self, value: str) -> str:
        """ Validates that the username is unique and not empty. """
        if not value:
            raise serializers.ValidationError("Username cannot be empty")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        if not value[0].isalpha():
            raise serializers.ValidationError("Username must start with a letter")
        return value


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
