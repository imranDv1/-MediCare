from django.contrib import admin
from .models import Notification, SystemSettings

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_type', 'message', 'user', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('message',)
    date_hierarchy = 'created_at'

@admin.register(SystemSettings)
class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ('key',)
