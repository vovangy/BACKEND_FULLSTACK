from django.db import models
from user.models import User
from chats.models import Chat

class Message(models.Model):
    message_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Участник", related_name="message")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name="Чат", related_name="message")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    viewed = models.BooleanField(default=False, verbose_name="Просмотрено")
    text = models.CharField(max_length=1000, verbose_name="Текст")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
# Create your models here.
