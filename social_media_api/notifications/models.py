from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')  # Who receives the notification
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions')  # Who performed the action
    verb = models.CharField(max_length=255)  # Describes the action, like "liked" or "commented"
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')  # Reference to the object (post, comment)
    created_at = models.DateTimeField(auto_now_add=True)  # When the action occurred
    unread = models.BooleanField(default=True)  # If the notification is unread

    def __str__(self):
        return f"Notification: {self.actor} {self.verb} {self.target} for {self.recipient}"