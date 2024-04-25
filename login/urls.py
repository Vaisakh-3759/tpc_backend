from . import views
from django.urls import path

urlpatterns = [
    path("login/", views.Login.as_view(),name="Log-in"),
    path("notification/", views.Notification_API.as_view(),name="notificaton"),
    path("admin/", views.AdminUpdate.as_view(),name="admin"),
    
]
