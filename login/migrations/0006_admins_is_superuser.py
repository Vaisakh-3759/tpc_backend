# Generated by Django 5.0.3 on 2024-05-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0005_remove_admins_is_superadmin_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="admins",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
