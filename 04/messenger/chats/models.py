from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    photo = models.CharField(null=True, max_length=500)
    name = models.CharField(max_length=30)

class Chat(models.Model):
    chat_id = models.IntegerField(primary_key=True)
    photo = models.CharField(null=True, max_length=500)
    users = models.ManyToManyField('User')
    messages = models.ManyToManyField('Message')

class Message(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    chat_id = models.ForeignKey(Chat, null=False, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)


