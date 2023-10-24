from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.views import APIView
from .serializers import *
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout

class UserRegistrationAPI(APIView):
    authentication_classes=[]
    permission_classes=[]

    def post(self,request):
        try:
            user=CustomUserCreationSerializer(data=request.data)
            if user.is_valid():
                user.save()
                return Response('ok',status=status.HTTP_201_CREATED)
            else:
                print('error',user.errors)
                return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error...',e)
            return Response('eror ',status=status.HTTP_400_BAD_REQUEST)
        
class UserLogin(APIView):
    authentication_classes=[]
    permission_classes=[]
    def post(self,request):
        print('data//,,,,',request.data)
        email=request.data['email']
        password=request.data['password']
        try:
            user=authenticate(request,email=email,password=password)
            if user:
                login(user)
                return Response('ok',status=status.HTTP_202_ACCEPTED)
            else:
                message = {"message":"Invalid Credential"}
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            message = {"message":"Invalid Credential"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET',])
def me(request):
    print('requsr',request)
    return JsonResponse({
        'id':request.user.id,
        'email':request.user.email,
        'name':request.user.name
    })

@api_view(['POST'])
def sent_friend_request(request,pk):
    user=CustomUser.objects.get(id=pk)

    check1=FriendShipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2=FriendShipRequest.objects.filter(created_for=user).filter(created_by=request.user)
    if not check1 or not check2:
        friendship_request=FriendShipRequest.objects.create(created_for=user,created_by=request.user)

        return Response('friendship request created',status=status.HTTP_201_CREATED)
    return Response('request already exit',status=status.HTTP_200_OK)

@api_view(['GET'])
def friends(request,pk):
    user=CustomUser.objects.get(id=pk)
    user_ser=CustomUserSerializer(user)
    requests=[]
    if user==request.user:
        requests=FriendShipRequest.objects.filter(created_for=request.user,status='Sent')
        req_ser=FriendShipRequestSerializer1(requests,many=True )
    
    friends=user.friends.all()
    friends_ser=CustomUserSerializer(friends,many=True)

    return Response({
        'user':user_ser.data,
        'friends':friends_ser.data,
        'requests':req_ser.data

    })

@api_view(['POST'])
def handle_request(request,pk,status):
    user=CustomUser.objects.get(id=pk)

    friends_request=FriendShipRequest.objects.filter(created_for=request.user).get(created_by=user)
    friends_request.status=status
    friends_request.save()

    user.friends.add(request.user)
    user.friend_count=user.friend_count+1
    user.save()
   
    request_user=request.user
    request_user.friend_count=request_user.friend_count+1
    request_user.save()

    return Response('ok')


        


