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
        fields = [
            "drive",
            "dr_id",
            "st_id"
        ]
        def create(self, validated_data):
            return AppliedDrives.objects.create(**validated_data)
        def update(self, instance, validated_data):
            instance.drive = validated_data.get('drive', instance.drive)
            instance.dr_id = validated_data.get('dr_id', instance.dr_id)
            instance.st_id = validated_data.get('st_id', instance.st_id)
            instance.save()
            return instance
            