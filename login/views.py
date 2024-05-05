from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf import settings
from django.shortcuts import render
from . serializers import *
from . models import *
from Drives import models 
from django.contrib.auth.hashers import check_password

class Login(APIView):
    def post(self, request):
        try:
            email_id = request.data.get('email')
            password = request.data.get('password')
            if not email_id or not password:
                return Response({"message": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

            user = Users.objects.filter(email=email_id).first()
            print(user)
            if not user:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

            if not (password == user.made_password):
                print(user.made_password)
                print(password)
                return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

            serializer = LoginSerializer(Users.objects.get(email=email_id))
            return Response({"message": "Login successful", "data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": f"An unexpected error occurred {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self,request):
        try:
            id = request.data.get('id')
            user = Users.objects.get(id=id)
            serializer = LoginSerializer(user,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"User details updated successfully","data":serializer.data},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":f"An unexpected error occurred {e}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class Admin(APIView):
    def post(self, request):
        try:
            serializer = AdminUpdateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"unexpected error occoured{e}"},status=status.HTTP_400_BAD_REQUEST)

class AdminUpdate(APIView):
    def post(self, request):
        try:
            serializer = AdminUpdateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"unexpected error occoured{e}"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        try:
            username = request.data.get('username')
            check_if_exists = Users.objects.filter(username = username).exists()
            if not check_if_exists:
                return Response({"message":"User doesnot exist"},status=status.HTTP_404_NOT_FOUND)
            else:
                for drive in Users.objects.filter(username=username):
                    drive.delete()
                return Response({"message":"user deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({"message":"Error occour"},status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self,request):
        try:
            username = request.data.get('username')
            check_if_exists = Users.objects.filter(username = username).exists()
            
            if not check_if_exists:
                return Response({"message":"User doesnot exist"},status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = AdminUpdateSerializer(Users.objects.get(username=username))
                return Response({"message":"User details","data":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message":f"Error occour{e}"},status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request):
        try:
            email = request.data.get('email')
            check_if_exists = Users.objects.filter(email = email).exists()
            if not check_if_exists:
                return Response({"message":"User doesnot exist"},status=status.HTTP_404_NOT_FOUND)
            else:
                user = Users.objects.get(email=email)
                serializer = LoginSerializer(user,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"User details updated successfully","data":serializer.data},status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message":f"Error occour{e}"},status=status.HTTP_400_BAD_REQUEST)
        
class Notification_API(APIView):
    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            notifications = Notification.objects.all()
            serializer = NotificationSerializer(notifications, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        