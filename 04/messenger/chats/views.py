from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Chat

@require_http_methods(['GET'])
def create_chat(request):
    return JsonResponse({'Chat created': "OK"})

@require_http_methods(['GET'])
def view_chat(request):
    b = Chat(chat_id=1, photo='/home/home/png')
    b.save()
    return JsonResponse({'Chat': "Messi"})

@require_http_methods(['GET'])
def view_list_chats(request):
    return JsonResponse({'Chats': 1})
# Create your views here.
