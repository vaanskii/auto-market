from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from cars.models import Car
from cars.serializers import CarSerializer
from .filters import CarFilter
from rest_framework.permissions import AllowAny

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    permission_classes = [AllowAny]