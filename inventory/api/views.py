from django.shortcuts import render
from rest_framework import viewsets
from .models import Drone, Camera
from .serializers import DroneSerializer, ReadDroneSerializer, CameraSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class CameraViewSet(viewsets.ModelViewSet):
    serializer_class = CameraSerializer
    queryset = Camera.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DroneViewSet(viewsets.ModelViewSet):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ReadDroneSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ReadDroneSerializer(queryset, many=True)
        return Response(serializer.data)

