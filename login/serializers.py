from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.hashers import check_password

from .models import *

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields ="__all__"
    def check(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            return user
        else:
            raise serializers.ValidationError("Invalid username or password.")
    
    def validation(self,data):
        email = data.get("email")
        password = data.get("password")
        user = Users.objects.get(email=email)
        if user is not None:
            if check_password(password, user.password):
                return user
            else:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Invalid username or password.")
class NotificationSerializer(serializers.Serializer):
    class Meta:
        model = Notification
        fields = [
            "user",
            "message",
            "is_read",
            "drive",
            "created_at"
            ]
    def create(self, validated_data):
        return Notification.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.message = validated_data.get("message", instance.message)
        instance.is_read = validated_data.get("is_read", instance.is_read)
        instance.drive = validated_data.get("drive", instance.drive)
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.save()
        return instance


class AdminUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

    def create(self, validated_data):
        return Users.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.is_superuser = validated_data.get("is_superuser", instance.is_superuser)
        instance.save()
        return instance
    def delete(self, instance):
        instance.delete()
        return instance