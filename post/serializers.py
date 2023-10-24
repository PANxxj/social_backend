from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','body','attachments','created_by','likes','like_count','created_at_formatted','comments_count','comments']
        depth=2

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields=['id','body','created_by','created_at_formatted']
        depth=1

class CommentSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields='__all__'

class PostSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
