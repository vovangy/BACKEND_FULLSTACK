from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.CharField(null=True, blank=True, max_length=500, verbose_name="Путь к фото")
    birthday = models.DateField(null=True, blank=True, verbose_name="День рождения")
    #name = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
# Create your models here.
