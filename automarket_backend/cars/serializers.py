from rest_framework import serializers
from .models import ImageModel, Car
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