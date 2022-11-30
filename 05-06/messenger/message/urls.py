from django.urls import path

from . import views

urlpatterns = [
    path('create', views.create_message),
    path('delete', views.delete_message),
    path('edit', views.edit_message),
]