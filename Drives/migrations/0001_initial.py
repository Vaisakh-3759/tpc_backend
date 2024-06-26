# Generated by Django 5.0.3 on 2024-04-24 05:05

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Drive",
            fields=[
                (
                    "drive_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.TextField(max_length=100, unique=True)),
                ("lpa", models.FloatField(default="")),
                ("description", models.TextField(default="")),
                ("date", models.DateField()),
                ("position", models.CharField(default="", max_length=100)),
                ("location", models.CharField(default="", max_length=100)),
                ("skills", models.TextField(default="")),
                ("gpa_limit", models.CharField(default="", max_length=10)),
                ("backlog", models.CharField(default="", max_length=10)),
                ("backlog_history", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="AppliedDrives",
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
                ("driv_id", models.TextField(max_length=400)),
                ("st_id", models.TextField(max_length=400)),
                ("applied_at", models.DateTimeField(auto_now_add=True)),
                (
                    "drive",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Drives.drive"
                    ),
                ),
            ],
        ),
    ]
