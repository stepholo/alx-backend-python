from rest_framework import permissions
from .models import Conversation, Message


class IsParticipantOfConversation(permissions.BasePermission):
    """Only participants of a conversation can view/update/delete it or its message"""

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Conversation):
            return request.user in obj.participants.all()
        if isinstance(obj, Message):
            return request.user in obj.conversation.participants.all()
        return False
