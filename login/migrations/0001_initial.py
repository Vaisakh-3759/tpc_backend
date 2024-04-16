# Generated by Django 5.0.3 on 2024-04-15 15:15

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Drives", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("username", models.CharField(max_length=255)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="Email Address"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="Last Name"),
                ),
                ("is_superuser", models.BooleanField(default=False)),
                ("last_login", models.DateTimeField(auto_now_add=True)),
                ("made_password", models.CharField(max_length=500, unique=True)),
                ("gpa", models.CharField(default=0, max_length=500)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="users_custom", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True, related_name="users_custom", to="auth.permission"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("is_read", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "drive",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Drives.drive"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="login.users"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Admins",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_superadmin", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="login.users"
                    ),
                ),
            ],
        ),
    ]
