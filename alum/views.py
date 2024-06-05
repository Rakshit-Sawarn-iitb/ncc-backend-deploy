from rest_framework import status
from rest_framework.views import APIView,Response
from django.shortcuts import render,get_object_or_404
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.http import HttpResponse
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound
User = get_user_model()

# Create your views here.

@api_view(['POST'])
def register_alum(request):
    if request.method == 'POST':
        serializer = alumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)