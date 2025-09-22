from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ("request", "Request Sent"),
        ("response", "Response Sent"),
    )
    
    sender = models.ForeignKey(User, related_name="sent_notifications", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_notifications", on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} → {self.receiver}: {self.message}"

