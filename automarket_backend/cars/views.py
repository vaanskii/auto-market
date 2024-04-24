from .choices import (MANUFACTURER_CHOICES, CAR_MODELS, TYPE, CATEGORIES, LOCATION, 
FUEL_TYPES, TRANSMISSION_TYPES, CYLINDERS, DOORS, DRIVE_WHEELS, WHEEL, 
AIRBAG_OPTIONS, CAR_COLORS, INTERIOR_MATERIAL, INTERIOR_COLORS)

from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from django.db.models import Q

from .forms import CarForm
from .serializers import CarSerializer, ChoiceSerializer, CarDetailSerializer
from .serializers import ChoiceSerializer
from .models import ImageModel, Car

class ChoicesAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        choices_data = {
            'manufacturer': [choice[0] for choice in MANUFACTURER_CHOICES],
            'car_model': {manufacturer: [model_name for model_name, _ in models] for manufacturer, models in CAR_MODELS},
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
        images = request.FILES.getlist('images[]')
        main_image_file = request.FILES.get('main_image') 
        car_instance = None

        if form.is_valid():
            car_instance = form.save(commit=False)
            car_instance.created_by = request.user

            # Handle the main image
            if main_image_file:
                main_image_instance = ImageModel.objects.create(image=main_image_file, created_by=request.user)
                car_instance.main_image = main_image_instance 

            car_instance.save()

            for image in images:
                image_instance = ImageModel.objects.create(image=image, created_by=request.user)
                car_instance.images.add(image_instance)

            serializer = CarSerializer(car_instance)
            return Response(serializer.data)
        else:
            errors = form.errors.as_json()
            return Response({'error': 'Failed to create car entry.', 'details': errors})

class CarsDetailsApiView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    def get(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            return Response({'car': CarDetailSerializer(car).data})
        except Car.DoesNotExist:
            raise NotFound('Car not found.')
        
class SimilarCarsAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        manufacturer = kwargs.get('manufacturer', '').lower()
        current_car_id = kwargs.get('pk', None)
        similar_cars = Car.objects.filter(manufacturer__iexact=manufacturer)
        if current_car_id:
            similar_cars = similar_cars.exclude(id=current_car_id)
        similar_cars = similar_cars[:5]
        serializer = CarSerializer(similar_cars, many=True)
        return Response(serializer.data)