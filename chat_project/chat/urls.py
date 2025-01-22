from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('chat/<str:username>/', views.chat_room, name='chat_room'),
]