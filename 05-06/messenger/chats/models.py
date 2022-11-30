from django.db import models
from user.models import User

class Chat(models.Model):
    chat_id = models.IntegerField(primary_key=True)
    photo = models.CharField(null=True,blank=True, max_length=500, verbose_name="Фото")
    title = models.CharField(null=True,blank=False, max_length=50, verbose_name="Название")
    description = models.CharField(blank=True, max_length=200, verbose_name="Описание")
    users = models.ManyToManyField(User, verbose_name="Участники", related_name="chats")
    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
