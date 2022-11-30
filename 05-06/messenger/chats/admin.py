from django.contrib import admin
from .models import Chat
class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'photo')
    list_filter = ('chat_id',)

admin.site.register(Chat, ChatAdmin)