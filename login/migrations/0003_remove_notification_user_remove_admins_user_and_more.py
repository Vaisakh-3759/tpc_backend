# Generated by Django 5.0.3 on 2024-04-17 11:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0002_remove_users_backlogs_remove_users_gpa_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notification",
            name="user",
        ),
        migrations.RemoveField(
            model_name="admins",
            name="user",
        ),
        migrations.DeleteModel(
            name="Users",
        ),
    ]