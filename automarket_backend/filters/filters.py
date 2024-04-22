import django_filters
from django_filters import NumberFilter

from cars.models import *

class CarFilter(django_filters.FilterSet):
    start_year = NumberFilter(field_name="year", lookup_expr='gte')
    end_year = NumberFilter(field_name="year", lookup_expr='lte')
    start_price = NumberFilter(field_name="price", lookup_expr='gte')
    end_price = NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Car
        fields = ('manufacturer', 'car_model', 'types', 'location', 'price', 'year')
