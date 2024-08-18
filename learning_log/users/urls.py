"""Define urls for users"""
from django.urls import path, include


app_name = 'users'
urlpatterns = [
    # Add basic URL for authentication
    path('', include('django.contrib.auth.urls')),
]