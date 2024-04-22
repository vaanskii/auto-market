from django.urls import path
from .views import CarList

urlpatterns = [
    path('filters/', CarList.as_view()),
]