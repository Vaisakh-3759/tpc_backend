from rest_framework import serializers
from .models import *
from rest_framework.response import Response
from rest_framework import status

class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = "__all__"
        def create(self, validated_data):
            return Drive.objects.create(**validated_data)
        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.lpa = validated_data.get('lpa', instance.lpa)
            instance.description = validated_data.get('description', instance.description)
            instance.date = validated_data.get('date', instance.date)
            instance.position = validated_data.get('position', instance.position)
            instance.location = validated_data.get('location', instance.location)
            instance.skills = validated_data.get('skills', instance.skills)
            instance.save()
            return instance
        
class AppliedDrivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedDrives
        fields = "__all__"
        def create(self, validated_data):
            return AppliedDrives.objects.create(**validated_data)
        def update(self, instance, validated_data):
            instance.subject = validated_data.get('subject', instance.subject)
            instance.message = validated_data.get('message', instance.message)
            instance.created_at = validated_data.get('created_at', instance.created_at)
            instance.save()
            return instance
            