# Generated by Django 5.0.3 on 2024-05-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0004_alter_notification_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="message",
            field=models.TextField(default="Notification", max_length=255),
        ),
    ]
