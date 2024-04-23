from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateCarsAPIView.as_view(), name='create-cars'),
    path('choices/', ChoicesAPIView.as_view(), name='api-choices'),
    path('<uuid:pk>/', CarsDetailsApiView.as_view(), name='api-car-details')
]
