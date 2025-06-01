from django.shortcuts import render
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response


class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Conversation model.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Message model.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']

    def perform_create(self, serializer: MessageSerializer) -> None:
        """Override to set the sender to the current user."""
        serializer.save(sender=self.request.user)

    @action(detail=False, methods=['get'])
    def custom_status(self, request: None) -> Response:
        """Example custom action using status."""
        return Response({'detail': 'Custom status OK'}, status=status.HTTP_200_OK)
