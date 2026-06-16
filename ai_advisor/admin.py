from django.contrib import admin
from .models import AIConsultation

@admin.register(AIConsultation)
class AIConsultationAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'truncated_query')
    list_filter = ('created_at', 'user')
    search_fields = ('query', 'response', 'user__username')
    date_hierarchy = 'created_at'

    def truncated_query(self, obj):
        return obj.query[:75] + '...' if len(obj.query) > 75 else obj.query
    truncated_query.short_description = 'Query'
