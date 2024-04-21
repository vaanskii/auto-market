from rest_framework import serializers
from .models import ImageModel, Car
from .choices import (MANUFACTURER_CHOICES, CAR_MODELS, TYPE, CATEGORIES, LOCATION, FUEL_TYPES, TRANSMISSION_TYPES, CYLINDERS, DOORS, 
                      DRIVE_WHEELS, WHEEL, AIRBAG_OPTIONS, CAR_COLORS, INTERIOR_MATERIAL, INTERIOR_COLORS)
from account.serializers import UserSerializer

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('id', 'get_image',)

class CarSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    images = ImageModelSerializer(read_only=True, many=True)
    class Meta:
        model = Car
        fields = ('id','manufacturer', 'car_model', 'types', 'categories', 'price', 'year', 'location', 'engine_volume',
                    'milage', 'fuel_type', 'transmission', 'cylinders', 'doors', 'drive_wheels', 'wheel', 'airbags',
                    'car_colors', 'interior', 'interior_color', 'description', 'images')
        
class ChoiceSerializer(serializers.Serializer):
    manufacturer = serializers.ChoiceField(choices=MANUFACTURER_CHOICES)
    car_model = serializers.ChoiceField(choices=CAR_MODELS)
    types = serializers.ChoiceField(choices=TYPE)
    categories = serializers.ChoiceField(choices=CATEGORIES)
    location = serializers.ChoiceField(choices=LOCATION)
    fuel_type = serializers.ChoiceField(choices=FUEL_TYPES)
    transmission = serializers.ChoiceField(choices=TRANSMISSION_TYPES)
    cylinders = serializers.ChoiceField(choices=CYLINDERS)
    doors = serializers.ChoiceField(choices=DOORS)
    drive_wheels = serializers.ChoiceField(choices=DRIVE_WHEELS)
    wheel = serializers.ChoiceField(choices=WHEEL)
    airbags = serializers.ChoiceField(choices=AIRBAG_OPTIONS) 
    car_colors = serializers.ChoiceField(choices=CAR_COLORS) 
    interior = serializers.ChoiceField(choices=INTERIOR_MATERIAL) 
    interior_color = serializers.ChoiceField(choices=INTERIOR_COLORS)
