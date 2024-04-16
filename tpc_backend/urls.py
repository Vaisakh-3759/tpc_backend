from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", include('login.urls')),
    path("password/", include('Password.urls')),
    path("drives/", include('Drives.urls')),
]

urlpatterns += staticfiles_urlpatterns()