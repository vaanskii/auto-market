from .choices import (MANUFACTURER_CHOICES, CAR_MODELS, TYPE, CATEGORIES, LOCATION, 
FUEL_TYPES, TRANSMISSION_TYPES, CYLINDERS, DOORS, DRIVE_WHEELS, WHEEL, 
AIRBAG_OPTIONS, CAR_COLORS, INTERIOR_MATERIAL, INTERIOR_COLORS)

from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .forms import ImageModelForm, CarForm
from .serializers import CarSerializer, ChoiceSerializer
from .serializers import ChoiceSerializer


class ChoicesAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        choices_data = {
            'manufacturer': [choice[0] for choice in MANUFACTURER_CHOICES],
            'car_model': [model[0] for model in CAR_MODELS],
            'types': [choice[0] for choice in TYPE],
            'categories': [choice[0] for choice in CATEGORIES],
            'location': [choice[0] for choice in LOCATION],
            'fuel_type': [choice[0] for choice in FUEL_TYPES],
            'transmission': [choice[0] for choice in TRANSMISSION_TYPES],
            'cylinders': [choice[0] for choice in CYLINDERS],
            'doors': [choice[0] for choice in DOORS],
            'drive_wheels': [choice[0] for choice in DRIVE_WHEELS],
            'wheel': [choice[0] for choice in WHEEL],
            'airbags': [choice[0] for choice in AIRBAG_OPTIONS],
            'car_colors': [choice[0] for choice in CAR_COLORS],
            'interior': [choice[0] for choice in INTERIOR_MATERIAL],
            'interior_color': [choice[0] for choice in INTERIOR_COLORS]
        }
        serializer = ChoiceSerializer(data=choices_data)
        serializer.is_valid()
        return Response(serializer.data)
    
class CreateCarsAPIView(APIView):
    def post(self, request, format=None):
        form = CarForm(request.POST)
        image = None
        image_form = ImageModelForm(request.POST, request.FILES)

        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.created_by = request.user
            image.save()

        if form.is_valid():
            cars = form.save(commit=False)
            cars.created_by = request.user
            cars.save()

            if image:
                cars.images.add(image)

            user = request.user
            user.save()

            serializer = CarSerializer(cars)

            return Response(serializer.data)
        else:
            errors = form.errors.as_json()
            if image_form.errors:
                errors += image_form.errors.as_json()
            return Response({'error': 'Failed to create car entry.', 'details': errors})
