from django.contrib import admin
from .models import Drone, Camera


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'serial_number']
    list_filter = ['name', 'brand']
    search_fields = ['name', 'brand']

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'mp_number']
    list_filter = ['name', 'brand', 'mp_number']
    search_fields = ['name', 'brand']
