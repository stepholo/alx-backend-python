from rest_framework import permissions
from .models import Conversation, Message


class IsParticipantOfConversation(permissions.BasePermission):
    """Custom permission to:
        - Allow only authenticated users
        - Allows only conversation participants to access messages and conversation
    """

    def has_permission(self, request, view):
        """Authenticate to access any view"""
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Tie messages to conversations"""
        if isinstance(obj, Conversation):
            return request.user in obj.participants.all()
        if isinstance(obj, Message):
            return request.user in obj.conversation.participants.all()
        return False
