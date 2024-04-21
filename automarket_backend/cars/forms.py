from django.forms import ModelForm
from .models import ImageModel, Car

class ImageModelForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = ('image',)

class CarForm(ModelForm):
    model = Car
    fields = ('manufacturer', 'car_model', 'types', 'categories', 'price', 'year', 'location', 'engine_volume',
              'milage', 'fuel_type', 'transmission', 'cylinders', 'doors', 'drive_wheels', 'wheel', 'airbags',
                'car_colors', 'interior', 'interior_color', 'description')