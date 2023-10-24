from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.views import APIView
from account.serializers import *
from account.models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

@api_view(["GET"])
def conversation_list(request):
    conversation=Conversation.objects.filter(users__in=list([request.user]))

    ser=ConversationSerializer(conversation,many=True)
    return Response(ser.data,status=status.HTTP_200_OK)


@api_view(["GET"])
def conversation_detail(request,pk):
    conversation=Conversation.objects.filter(users__in=list([request.user])).get(id=pk)

    ser=ConversationDetailser(conversation)
    return Response(ser.data,status=status.HTTP_200_OK)


@api_view(["POST"])
def conversation_send_messages(request,pk):
    conversation=Conversation.objects.filter(users__in=list([request.user])).get(id=pk)

    for user in conversation.users.all():
        if user != request.user:
            sent_to =user
    conversation_messages=ConversationMessage.objects.create(
        conversation=conversation,
        body=request.data['body'],
        created_by=request.user,
        sent_to=sent_to
    )
    ser=ConversationMessageSerializer(conversation_messages)
    return Response(ser.data,status=status.HTTP_200_OK)

@api_view(["POST"])
def conversation_get_or_create(request,pk):
    try:
        user=CustomUser.objects.filter(id=pk)
        print('ok',user,'ok',request.user.id)
        conversations=Conversation.objects.filter(users__in=list([request.user.id])).filter(users__id__in=list([pk]))
        print('ok')

        if conversations.exists():
            conversation=conversations.first()
            print('ok')
        else:
            conversation=Conversation.objects.create()
            print('ok')
            conversation.users.add(pk,request.user)
            conversation.save()
        ser=ConversationDetailser(conversation)
        return Response(ser.data,status=status.HTTP_200_OK)
    except Exception as e :
        print('error ./././././././.',e,'./././././././././,.')
        return Response('eror',status=status.HTTP_400_BAD_REQUEST)


