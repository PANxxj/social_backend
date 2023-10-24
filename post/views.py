from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.views import APIView
from account.serializers import *
from account.models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class PostAPI(APIView):
    def get(self,request):
        try:
            user_ids=[request.user]

            for user in request.user.friends.all():
                user_ids.append(user.id)
            post=Post.objects.filter(created_by__in=user_ids)
            post_ser=PostSerializer(post,many=True)
            return Response(post_ser.data,status=status.HTTP_200_OK)
        except Exception as e :
            print('error',e)
            return Response('error',status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):
        ser=PostSerializer1(data=request.data)
        if ser.is_valid():
            ser.save(created_by=request.user)
            posts=Post.objects.all()
            posts_ser=PostSerializer(posts,many=True)
            return Response(posts_ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PostProfileAPI(APIView):
    def get(self,request,pk):
        user=CustomUser.objects.get(id=pk)
        user_ser=CustomUserSerializer(user)
        post=Post.objects.filter(created_by_id=pk)
        ser=PostSerializer(post,many=True)
        context={
            'user':user_ser.data,
            'post':ser.data
        }
        return Response(context,status=status.HTTP_200_OK)
    

# Search 

@api_view(['POST'])
def search(request):
    query=request.data['query']
    users=CustomUser.objects.filter(name__icontains=query)
    ser=CustomUserSerializer(users,many=True)
    post=Post.objects.filter(body__icontains=query)
    post_ser=PostSerializer(post,many=True)
    context={
        'users':ser.data,
        'posts':post_ser.data
    }
    return Response(context,status=status.HTTP_200_OK)

@api_view(["POST"])
def like_post(request,pk):
    post=Post.objects.get(id=pk)

    if not post.likes.filter(created_by =request.user):
        like=Likes.objects.create(created_by=request.user)

        post=Post.objects.get(id=pk)
        post.like_count+=1
        post.likes.add(like)
        post.save()
        return Response('like created',status=status.HTTP_200_OK)
    return Response('already like',status=status.HTTP_200_OK)


@api_view(['GET'])
def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    ser=PostSerializer(post)
    comment=post.comments.all()
    comment_ser=CommentSerializer(comment,many=True)
    return Response({'data':ser.data,'comments':comment_ser.data},status=status.HTTP_200_OK)

@api_view(['POST'])
def post_create_comment(request,pk):
    comment=Comments.objects.create(body=request.data['body'],created_by=request.user)

    post=Post.objects.get(id=pk)
    post.comments_count+=1
    post.comments.add(comment)
    post.save()
    ser=CommentSerializer(comment)
    return Response(ser.data,status=status.HTTP_201_CREATED)
