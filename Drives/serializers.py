from rest_framework import serializers
from .models import *

class DriveSerializer(serializers.Serializer):
    class meta :
        model = Drive
        fields = [
            "name",
            "drive_id",
        ]
    def create(self, validated_data):
        return Drive.objects.create(**validated_data)
    def update(self, validated_data, instance):
        instance.name = validated_data.get('name', instance.name)
        instance.drive_id = validated_data.get('drive_id', instance.drive_id)
        instance.save()
        return instance
    def delete(self, instance):
        instance.delete()
        return instance
