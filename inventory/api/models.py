from django.db import models

class Camera(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=True)
    brand = models.CharField(max_length=32, blank=True)
    mp_number = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    def __str__(self):
        return '%s %s' %(self.brand, self.name)

class Drone(models.Model):
    name = models.CharField(max_length=32, unique=True)
    brand = models.CharField(max_length=32)
    serial_number = models.CharField(max_length=32, blank=True)
    supported_cameras = models.ManyToManyField(Camera, related_name='supported_cameras', blank=True)
    description = models.CharField(max_length=100, blank=True)
