from django.urls import path

from . import views

urlpatterns = [
    path('create', views.create_chat),
    path('list', views.view_list_chats),
    path('', views.view_chat),
]
