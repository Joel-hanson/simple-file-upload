from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r"", include(("app_name.urls", "app_name"), namespace="api")),
]
