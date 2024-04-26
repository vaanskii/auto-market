from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateCarsAPIView.as_view(), name='create-cars'),
    path('choices/', ChoicesAPIView.as_view(), name='api-choices'),
    path('<uuid:pk>/', CarsDetailsApiView.as_view(), name='api-car-details'),
    path('similar/<str:manufacturer>/<uuid:pk>/', SimilarCarsAPIView.as_view(), name='similar-cars'),
    path('recently/', RecentlyAddedCarsAPIView.as_view(), name='recently-cars'),
    path('profile/cars/<uuid:id>/', UserCarsAPIView.as_view(), name="user-cars"),
    path('delete/<uuid:id>/', DeleteCarAPIView.as_view(), name='delete-car')
]