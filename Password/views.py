from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings

class CustomPasswordResetView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if email:
            UserModel = get_user_model()
            try:
                user = UserModel._default_manager.get(email=email)
            except UserModel.DoesNotExist:
                return Response(status=status.HTTP_200_OK)
            uid = urlsafe_base64_encode(force_str(user.pk).encode())
            token = default_token_generator.make_token(user)
            send_mail(
                "Password reset",
                f"Click here to reset your password: http://localhost:3000/reset/{uid}/{token}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
        return Response(status=status.HTTP_200_OK)
    