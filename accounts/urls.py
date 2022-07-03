from django.urls import path, include
from .api import SimpleApi, RegistrationApi

urlpatterns = [
    path('api/hello', SimpleApi.as_view()),
    path('api/register', RegistrationApi.as_view())
]