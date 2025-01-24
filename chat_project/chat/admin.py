from django.contrib import admin
from .models import ChatMessage

# Register your models here.

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'timestamp', 'is_read')
    list_filter = ('sender', 'receiver', 'is_read')
    search_fields = ('message', 'sender__username', 'receiver__username')
    date_hierarchy = 'timestamp'