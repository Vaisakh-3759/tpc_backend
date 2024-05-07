from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from . serializers import *
from . models import AppliedDrives, Drive
from login.models import Users

class Drive_API(APIView):
    def post(self, request):
        try:
            name = request.data.copy()
            print(name)
            serializer = DriveSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Drive creation successfull"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            drive_instance = request.data.get('drive_id')
            check_if_exists = Drive.objects.filter(drive_id = drive_instance).exists()
            if not check_if_exists:
                return Response({"message":"Drive doesnot exist"},status=status.HTTP_404_NOT_FOUND)
            else:
                for drive in Drive.objects.filter(drive_id=drive_instance):
                    drive.delete()
                return Response({"message":"Drive deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({"message":"Error occour"},status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            id = request.data.get('drive_id')
            user = Drive.objects.get(drive_id=id)
            serializer = DriveSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        try:
            drives = Drive.objects.all()
            serializer = DriveSerializer(drives, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AppliedDrives_API(APIView):

    def post(self, request):
        try:
            serializer = AppliedDrivesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request):
        try:
            std_id = request.query_params.get('st_id')
            applied_drives = AppliedDrives.objects.filter(st_id = std_id)
            serializer = AppliedDrivesSerializer(applied_drives, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        try:
            drive_id = request.data.get('drive_id')
            serializer = AppliedDrivesSerializer(AppliedDrives.objects.filter(drive_id=drive_id), many=True)
            st_ids = [serializer.data[i]['st_id'] for i in range(len(serializer.data))]
            for id in st_ids:
                userserializer = UserSerializer(Users.objects.filter(id=id), many=True)
            return Response(userserializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)