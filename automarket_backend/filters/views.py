from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from cars.models import Car
from .serializers import CarSerializer
from .filters import CarFilter

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter