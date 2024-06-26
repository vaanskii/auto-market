from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('user/', UserAPIView.as_view(), name='user'),
    path('editprofile/', EditProfileAPIView.as_view(), name='edit-profile'),
    path('changepassword/', PasswordChangeAPIView.as_view(), name="change-password"),
    path('forgot/', ForgotPasswordAPIView.as_view(), name="forgot-password"),
    path('reset/', ResetPasswordAPIView.as_view(), name="reset-password"),
]
