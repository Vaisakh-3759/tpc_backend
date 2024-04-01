from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf import settings
from django.shortcuts import render
from . serializers import *
from . models import *
from Drives import models as drive_models

class Login(APIView):
    def get(self,request):
        try:
            email = request.data['email']
            passwd = request.data['password']
            user_data = Users.objects.get(username = email)
            check_if_exists = Users.objects.filter(username = email).exists()
            if check_if_exists:
                serializer = LoginSerializer(user_data)
                if user_data.password == passwd:
                    return Response({"message":"Login successfull","data":serializer.data},status=status.HTTP_200_OK)
                else:
                    return Response({"message":"Invalid password"},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message":"Username doesnot exist"},status=status.HTTP_404_NOT_FOUND)
                        
        except Exception as e:
            return Response({"message": f"unexpected error occoured(e)"},status=status.HTTP_400_BAD_REQUEST)


class Notification_API(APIView):
    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)