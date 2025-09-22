from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by("-created_at")
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show notifications for the logged-in user
        return Notification.objects.filter(receiver=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        # Sender is the logged-in user
        serializer.save(sender=self.request.user)
