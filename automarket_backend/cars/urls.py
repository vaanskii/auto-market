from django.urls import path
from . import views
from .views import ChoicesAPIView

urlpatterns = [
    path('create/', views.create_cars, name='create-cars'),
    path('choices/', ChoicesAPIView.as_view(), name='api-choices')
]
