# Generated by Django 5.0.3 on 2024-05-04 19:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Drives", "0004_rename_backlog_drive_backlog_limit"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="applieddrives",
            name="driv_id",
        ),
        migrations.RemoveField(
            model_name="applieddrives",
            name="id",
        ),
        migrations.AddField(
            model_name="applieddrives",
            name="apply_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AddField(
            model_name="drive",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
