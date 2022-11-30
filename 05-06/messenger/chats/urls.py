from django.urls import path

from . import views

urlpatterns = [
    path('create', views.create_chat),
    path('list', views.view_list_chats),
    path('', views.chat_info),
    path('delete', views.delete_chat),
    path('edit', views.edit_chat),
    path('appenduser', views.append_chat_user),
    path('removeuser', views.delete_chat_user),
    path('messages', views.chat_messages),
]
