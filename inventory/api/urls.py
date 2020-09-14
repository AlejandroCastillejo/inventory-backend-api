from django.urls import path, include
from rest_framework import routers
from .views import DroneViewSet, CameraViewSet

router = routers.DefaultRouter()
router.register('drones', DroneViewSet)
router.register('cameras', CameraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]