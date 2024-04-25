from django.db import models
import uuid
from datetime import date

class Drive(models.Model):
    drive_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(unique = True ,max_length = 100,null = False)
    lpa = models.FloatField(default='',null = False)
    description = models.TextField(default='',null = False)
    lastdate = models.DateField(default="2024-4-24")
    drivedate = models.DateField(default="2024-4-24")
    position = models.CharField(default="",max_length = 100)
    location = models.CharField(default="",max_length = 100)
    skills = models.TextField(default='',null = False)
    gpa_limit = models.CharField(default='',null = False,max_length = 10)
    backlog = models.CharField(default='',null = False,max_length = 10)
    backlog_history = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    
class AppliedDrives(models.Model):
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE)
    driv_id = models.TextField(max_length=400)
    st_id = models.TextField(max_length=400)
    applied_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} applied for {self.drive.name}"