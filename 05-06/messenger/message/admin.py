from django.contrib import admin
from .models import Message
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'user')
    list_filter = ('chat',)

admin.site.register(Message, MessageAdmin)

# Register your models here.
