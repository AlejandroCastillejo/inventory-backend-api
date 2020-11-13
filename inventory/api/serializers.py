from rest_framework import serializers
# from django.db import models
from .models import Drone, Camera

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'name', 'brand', 'mp_number']

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ['name', 'brand', 'serial_number', 'supported_cameras']

class ReadDroneSerializer(serializers.ModelSerializer):
    # supported_cameras = CameraSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()
     
    def get_description(self, obj):
        camera_names = []
        cameras = obj.supported_cameras.get_queryset()
        for camera in cameras:
            camera_names.append(camera.name)
        # return '...description'
        return ('Suported cameras: ', camera_names)

    class Meta:
        model = Drone
        fields = ['id', 'name', 'brand', 'serial_number', 'description']
