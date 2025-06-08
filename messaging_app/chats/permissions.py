from rest_framework import permissions


class IsParticipant(permissions.BasePermission):
    """Allows access only to participants of the conversation"""

    def has_object_permission(self, request: any, view: any, obj: any) -> any:
        """Returns all user objects"""
        return request.user in obj.participants.all()


class IsSenderOrReceiver(permissions.BasePermission):
    """Allow access only to sender or receiver of the message"""

    def has_object_permission(self, request: any, view: any, obj: any) -> any:
        """Allows access only to sender or receiver of the message"""
        return obj.sender == request.user or obj.receiver == request.user
