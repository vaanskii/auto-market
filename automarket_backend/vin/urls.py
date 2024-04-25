from django.urls import path
from .views import *

urlpatterns = [
    path('vin/', VinDecoderView.as_view(), name='vin-decode')
]
