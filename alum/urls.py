from django.urls import path
from .views import register_alum

urlpatterns = [
    path('register/', register_alum, name='alumRegistration')
]