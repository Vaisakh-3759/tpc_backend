from django.urls import path
from . import views

urlpatterns = [
    path("drive/", views.Drive_API.as_view(),name="Log-in"),
    path("apply-drive/", views.AppliedDrives_API.as_view(),name="notificaton"),
    
]
