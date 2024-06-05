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

@api_view(['GET'])
def api_cards(request):
    if request.method=='GET':
        cards = CouncilCard.objects.all()
        serializers = CardSerializer(cards, many=True)
        return Response(serializers.data)