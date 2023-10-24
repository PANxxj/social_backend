from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


class CustomUserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['id','name','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate_password(self,value):
        validate_password(value)
        return value
    
    def create(self,validated_data):
        user=get_user_model()(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'


class FriendShipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=FriendShipRequest
        fields='__all__'
        
class FriendShipRequestSerializer1(serializers.ModelSerializer):
    class Meta:
        model=FriendShipRequest
        fields='__all__'
        depth=1