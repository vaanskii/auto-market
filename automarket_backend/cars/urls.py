from django.urls import path
from .views import ChoicesAPIView, CreateCarsAPIView

urlpatterns = [
    path('create/', CreateCarsAPIView.as_view(), name='create-cars'),
    path('choices/', ChoicesAPIView.as_view(), name='api-choices')
]
