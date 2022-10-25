from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def create_chat(request):
    return JsonResponse({'Chat created': "OK"})

@require_http_methods(['GET'])
def view_chat(request):
    return JsonResponse({'Chat': "Messi"})

@require_http_methods(['GET'])
def view_list_chats(request):
    return JsonResponse({'Chats': 1})
# Create your views here.
