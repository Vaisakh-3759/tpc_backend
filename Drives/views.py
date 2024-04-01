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
        serializer = DriveSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk):
        drive = self.get_object(pk)
        serializer = DriveSerializer(drive, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self,pk):
        drive = self.get_object(pk)
        drive.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)