from django.db import models
from django.conf import settings

class Notification(models.Model):
    TYPE_CHOICES = [
        ('low_stock', 'Low Stock'),
        ('expired', 'Expired'),
        ('near_expiry', 'Near Expiry'),
        ('new_sale', 'New Sale'),
        ('system', 'System'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications'
    )
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_notification_type_display()}] {self.message[:50]}"


class SystemSettings(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    class Meta:
        verbose_name_plural = 'System Settings'

    def __str__(self):
        return f"{self.key}: {self.value[:50]}"
