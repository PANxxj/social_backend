from django.urls import path
from .views import *

urlpatterns =[
    path('conversation_list/',conversation_list,name='conversation_list'),
    path('conversation_detail/<int:pk>',conversation_detail,name='conversation_detail'),
    path('send_messages/<int:pk>',conversation_send_messages,name='conversation_send_messages'),
    path('chat/get_or_create/<int:pk>',conversation_get_or_create,name='conversation_get_or_create'),
]