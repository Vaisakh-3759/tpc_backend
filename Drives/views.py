from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from . serializers import *
from . models import *

class Drive_API(APIView):
    def post(self, request):
        try:
            name = request.data()
            print(name)
            serializer = DriveSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            drive_instance = request.data.get('name')
            for drive in Drive.objects.filter(name=drive_instance):
                drive.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            drive_instance = request.data.get('name')
            new_name = request.data.get('new_name')
            for drive in Drive.objects.filter(name=drive_instance):
                drive.name = new_name
                drive.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Apply_API(APIView):
    def post(self, request):
        try:
            drive_instance = request.data()
            
            serializer = AppliedDrivesSerializer(drive_instance)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
