from rest_framework import serializers
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
    supported_cameras = CameraSerializer(many=True, read_only=True)
    class Meta:
        model = Drone
        fields = ['name', 'brand', 'serial_number', 'supported_cameras']