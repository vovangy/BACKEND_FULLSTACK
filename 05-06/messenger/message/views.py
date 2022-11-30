from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Message
from chats.models import Chat
from user.models import User
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(['POST'])
def create_message(request):
    data = json.loads(request.body)
    if ("user" not in data.keys() or "chat" not in data.keys() or "text" not in data.keys()):
        return JsonResponse({'Error': "not chat or user or text in the passed arguments"})
    if (not str(data["chat"]).isdigit() or not str(data["user"]).isdigit()):
        return JsonResponse({'Error': "user and chat must be digits"})
    user = get_object_or_404(User, id=data["user"])
    chat = get_object_or_404(Chat, chat_id=data["chat"])
    message = Message.objects.create(message_id = len(Message.objects.all()) + 1, user = user, chat = chat, text = data["text"])
    return JsonResponse({'Message created': 1}, status=201)


@csrf_exempt
@require_http_methods(['POST'])
def edit_message(request):
    data = json.loads(request.body)
    if "message_id" not in data.keys():
        return JsonResponse({"Error": "not message_id in the passed arguments"}, status=400)
    if (not str(data["message_id"]).isdigit()):
        return JsonResponse({'Error': "message_id must be digit"}, status=400)
    message = get_object_or_404(Message, message_id= data["message_id"])
    if "viewed" in data.keys():
        message.viewed = data["viewed"]
    if "text" in data.keys():
        message.text = data["text"]
    message.save()
    return JsonResponse({"Message edited": 1}, status=201)
# Create your views here.

@csrf_exempt
@require_http_methods(['POST'])
def delete_message(request):
    data = json.loads(request.body)
    if ("message_id" not in data.keys()):
        return JsonResponse({'Error': "not message_id in the passed arguments"}, status=400)
    if (not str(data["message_id"]).isdigit()):
        return JsonResponse({'Error': "message_id must be digit"}, status=400)
    message = get_object_or_404(Message, message_id=data["message_id"])
    message.delete()
    return JsonResponse({"Message removed": 1}, status=201)
