from django.shortcuts import render
from .models import User,Usage
from .serializers import *
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter
class UserModelViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter]
class UsageModelViewset(viewsets.ModelViewSet):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]   
    filterset_fields = ['date_created']