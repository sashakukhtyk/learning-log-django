"""Define urls for users"""
from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # Add basic URL for authentication
    path("", include("django.contrib.auth.urls")),
    path("logout", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
]