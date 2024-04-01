from django.db import models
import uuid

class Drive(models.Model):
    drive_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)