from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(actor, recipient, verb, target):
    Notification.objects.create(
        actor=actor,
        recipient=recipient,
        verb=verb,
        content_type=ContentType.objects.get_for_model(target),
        object_id=target.id
    )
