# serializers.py
from rest_framework import serializers
from cars.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['manufacturer', 'car_model', 'types', 'location', 'year', 'price']
