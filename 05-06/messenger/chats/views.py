from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from message.models import Message
from .models import Chat
from user.models import User
import json
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(['POST'])
def create_chat(request):
    data = json.loads(request.body)
    if ("user1" not in data.keys() or "user2" not in data.keys() or "title" not in data.keys()):
        return JsonResponse({'Error': "not user1 or user2 or title in the passed arguments"}, status=400)
    if (not str(data["user1"]).isdigit() or not str(data["user2"]).isdigit()):
        return JsonResponse({'Error': "user1 and user2 must be digits"}, status=400)
    user1 = get_object_or_404(User, id=data["user1"])
    user2 = get_object_or_404(User, id=data["user2"])
    chat = Chat.objects.create(chat_id = len(Chat.objects.all()) + 1, title = data["title"])
    if ("description" in data.keys()):
        chat.description = data["description"]
    if ("photo" in data.keys()):
        chat.photo = data["photo"]
    chat.users.add(user1, user2)
    return JsonResponse({'Succes': "Chat created"}, status=201)

@csrf_exempt
@require_http_methods(['POST'])
def delete_chat(request):
    data = json.loads(request.body)
    if ("chat_id" not in data.keys()):
        return JsonResponse({'Error': "not chat_id in the passed arguments"}, status=400)
    if (not str(data["chat_id"]).isdigit()):
        return JsonResponse({'Error': "chat_id must be digit"}, status=400)
    chat = get_object_or_404(Chat, chat_id=data["chat_id"])
    chat.delete()
    return JsonResponse({'Succes': "Chat deleted"}, status=201)
@require_http_methods(['GET'])
def chat_info(request):
    data = json.loads(request.body)
    if ("chat_id" not in data.keys()):
        return JsonResponse({'Error': "not chat_id in the passed arguments"}, status=400)
    if (not str(data["chat_id"]).isdigit()):
        return JsonResponse({'Error': "chat_id must be digit"}, status=400)
    chat = get_object_or_404(Chat, chat_id=data["chat_id"])
    result_chat={"photo":chat.photo, "title":chat.title, "description":chat.description, "users":[]}
    users = Chat.objects.get(chat_id=data["chat_id"]).users.all()
    for i in users:
        result_chat["users"].append(list((i.id, i.username)))
    return JsonResponse({'Chat': result_chat})

@require_http_methods(['GET'])
def view_list_chats(request):
    chats = {}
    for chat in Chat.objects.all():
        users = Chat.objects.get(chat_id = chat.chat_id).users.all()
        chats[chat.chat_id] = ([chat.chat_id, chat.photo, list()])
        for user in users:
            chats[user.chat_id][-1].append(list((user.id, user.username)))
    return JsonResponse({"Chats":chats}, status=200)# Create your views here.

@require_http_methods(['GET'])
def chat_messages(request):
    data = json.loads(request.body)
    if ("chat_id" not in data.keys()):
        return JsonResponse({'Error': "not chat_id in the passed arguments"}, status=400)
    if (not str(data["chat_id"]).isdigit()):
        return JsonResponse({'Error': "chat_id must be digit"}, status=400)
    messages = Message.objects.all()
    result_messages = []
    for message in messages:
        if message.chat.chat_id == data["chat_id"]:
            result_messages.append(dict(
            user=message.user.username,
            text=message.text,
            created=message.created,
            viewed=message.viewed,
            ))
    return JsonResponse({"Messages": result_messages})

@csrf_exempt
@require_http_methods(['POST'])
def edit_chat(request):
    data = json.loads(request.body)
    if "chat_id" not in data.keys():
        return JsonResponse(status=400, data={"Error": "not chat_id in the passed arguments"})
    if (not str(data["chat_id"]).isdigit()):
        return JsonResponse({'Error': "chat_id must be digit"}, status=400)
    chat = get_object_or_404(Chat, chat_id= data["chat_id"])
    if "title" in data.keys():
        chat.title = data["title"]
    if "description" in data.keys():
        chat.description = data["description"]
    if "photo" in data.keys():
        chat.photo = data["photo"]
    chat.save()
    return JsonResponse({"Succes": "Chat has been edited"}, status=201)

@csrf_exempt
@require_http_methods(['POST'])
def append_chat_user(request):
    data = json.loads(request.body)
    if ("chat_id" not in data.keys() or "user_id" not in data.keys()):
        return JsonResponse({'Error': "not chat_id or user_id in the passed arguments"}, status=400)
    if (not str(data["chat_id"]).isdigit()) or (not str(data["user_id"]).isdigit()):
        return JsonResponse({'Error': "chat_id and user_id must be digit"}, status=400)
    chat = get_object_or_404(Chat, chat_id=data["chat_id"])
    user = get_object_or_404(User, id=data["user_id"])
    users = Chat.objects.get(chat_id=data["chat_id"]).users.all()
    for usr in users:
        if usr.id == usr.id:
            return JsonResponse({'Error': "Such user already exists"}, status=200)
    chat.users.add(user)
    return JsonResponse({'Succes': "User appended"}, status=200)
@csrf_exempt
@require_http_methods(['POST'])
def delete_chat_user(request):
    data = json.loads(request.body)
    if ("chat_id" not in data.keys() or "user_id" not in data.keys()):
        return JsonResponse({'Error': "not chat_id or user_id in the passed arguments"}, status=400)
    if (not str(data["chat_id"]).isdigit()) or (not str(data["user_id"]).isdigit()):
        return JsonResponse({'Error': "chat_id and user_id must be digit"}, status=400)
    chat = get_object_or_404(Chat, chat_id=data["chat_id"])
    user = get_object_or_404(User, id=data["user_id"])
    users = Chat.objects.get(chat_id=data["chat_id"]).users.all()
    flag = 0
    for i in users:
        if i.id == user.id:
            flag = 1
            break
    if flag == 0:
        return JsonResponse({'Error': "This user does not exist"}, status=400)
    chat.users.remove(user)
    return JsonResponse({'Succes':"User removed"}, status=201)
