# Generated by Django 4.1.2 on 2022-11-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0007_delete_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='chat',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
