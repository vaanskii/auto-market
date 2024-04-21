from django.db import models
import uuid
from .choices import (MANUFACTURER_CHOICES, CAR_MODELS, TYPE, CATEGORIES, LOCATION, FUEL_TYPES, TRANSMISSION_TYPES, CYLINDERS, DOORS, 
                      DRIVE_WHEELS, WHEEL, AIRBAG_OPTIONS, CAR_COLORS, INTERIOR_MATERIAL, INTERIOR_COLORS)

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')

class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manufacturer = models.CharField(max_length=100, choices=MANUFACTURER_CHOICES[0], blank=False, null=False)
    car_model = models.CharField(max_length=100, choices=CAR_MODELS, blank=False, null=False)
    types = models.CharField(max_length=20, default='', choices=TYPE, blank=False, null=False)
    categories = models.CharField(max_length=30, default='', choices=CATEGORIES, blank=False, null=False)
    price = models.IntegerField(default='0', blank=False, null=False)
    year = models.IntegerField(default='2024', blank=False, null=False)
    location = models.CharField(max_length=40, default='Tbilisi', choices=LOCATION, blank=False, null=False)
    engine_volume = models.IntegerField(default='0', blank=True, null=True)
    milage = models.IntegerField(default='0', blank=False, null=False)
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPES, default='Petrol', blank=True, null=True)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_TYPES, default='Automatic', blank=False, null=False)
    cylinders = models.CharField(max_length=50, choices=CYLINDERS, default='8', blank=True, null=True)
    doors = models.CharField(max_length=50, choices=DOORS, default='4', blank=True, null=True)
    drive_wheels = models.CharField(max_length=50, choices=DRIVE_WHEELS, default='Rear', blank=True, null=True)
    wheel = models.CharField(max_length=50, choices=WHEEL, default='Left', blank=True, null=True)
    airbags = models.CharField(max_length=50, choices=AIRBAG_OPTIONS, default='1', blank=True, null=True)
    images = models.ManyToManyField('ImageModel')
    car_colors = models.CharField(max_length=20, choices=CAR_COLORS, default='Black', blank=False, null=False)
    interior = models.CharField(max_length=20, choices=INTERIOR_MATERIAL, default='Alcantara', blank=False, null=False)
    interior_color = models.CharField(max_length=20, choices=INTERIOR_COLORS, default='Black', blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)