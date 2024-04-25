from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('user/', UserAPIView.as_view(), name='user'),
    path('editprofile/', EditProfileAPIView.as_view(), name='edit-profile')
]
