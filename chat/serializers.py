from rest_framework import serializers
from .models import *

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Conversation
        fields=['id','created_at','modified_at_formatted','users']
        depth=1

class ConversationSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Conversation
        fields="__all__"

class ConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConversationMessage
        fields=['id','conversation','body','sent_to','created_by','created_at_formatted']
        depth=1

class ConversationMessageSerializer1(serializers.ModelSerializer):
    class Meta:
        model=ConversationMessage
        fields="__all__"

class ConversationDetailser(serializers.ModelSerializer):
    messages=ConversationMessageSerializer(read_only=True,many=True)

    class Meta:
        model=Conversation
        fields=['id','created_at','modified_at_formatted','messages']
        # depth=1

