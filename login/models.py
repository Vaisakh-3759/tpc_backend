from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
import uuid
from django.utils import timezone

class Users(models.Model):
    username = models.CharField(unique= True,max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True, verbose_name=_('Email Address'))
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    made_password = models.CharField(max_length=500, null=False)
    backlogs = models.IntegerField(default=0)
    gpa = models.FloatField(default=0)
    backlog_history = models.BooleanField(default=False)
    department = models.CharField(max_length=255, default="CSE")
    groups = models.ManyToManyField(Group, related_name='users_custom', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='users_custom', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.made_password = make_password(self.made_password)
        super(Users, self).save(*args, **kwargs)


    def __str__(self):
        return self.email

class Admins(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email
class Notification(models.Model):
    message = models.TextField(default="message")
    created_at = models.DateField(default=timezone.now)
    subjects = models.CharField(max_length=255, default="Notification")
