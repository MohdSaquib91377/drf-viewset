from functools import partial
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets

from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):
        serializer = UserSerializer(self.queryset,many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def retrieve(self, request,pk = None):
        user = get_object_or_404(self.queryset,pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(obj,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None):
        obj =  get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(obj,data = request.data,partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        obj.delete()
        return Response({"status":"400","message":"User delted successfully"},status=400)