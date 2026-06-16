from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Notification


@login_required
def notification_list(request):
    notifications = Notification.objects.filter(
        user=request.user
    ) | Notification.objects.filter(user__isnull=True)
    notifications = notifications.distinct()
    unread_count = notifications.filter(is_read=False).count()

    ntype = request.GET.get('type', '')
    if ntype:
        notifications = notifications.filter(notification_type=ntype)

    return render(request, 'notifications/notification_list.html', {
        'notifications': notifications,
        'unread_count': unread_count,
    })


@login_required
def mark_as_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    if notification.user is None or notification.user == request.user:
        notification.is_read = True
        notification.save()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok'})
    return redirect('notification_list')


@login_required
def mark_all_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    messages.success(request, 'All notifications marked as read.')
    return redirect('notification_list')


@login_required
def delete_notification(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    if notification.user is None or notification.user == request.user:
        notification.delete()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok'})
    return redirect('notification_list')


def create_notification(notification_type, message, user=None):
    Notification.objects.create(
        notification_type=notification_type,
        message=message,
        user=user
    )
