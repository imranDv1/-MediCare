from .models import Notification


def unread_notifications(request):
    if request.user.is_authenticated:
        count = Notification.objects.filter(
            is_read=False
        ).filter(
            user=request.user
        ).count()
        return {'unread_notifications_count': count}
    return {'unread_notifications_count': 0}
