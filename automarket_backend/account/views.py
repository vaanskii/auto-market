from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import SignupForm, ProfileForm
from .models import User

class UserAPIView(APIView):
    def get(self, request):
        if hasattr(request.user, 'mobile_number'):
            mobile_number = str(request.user.mobile_number)
        else:
            mobile_number = None

        data = {
            'id': request.user.id,
            'name': request.user.name,
            'email': request.user.email,
            'mobile_number': mobile_number,
            'country_code': request.user.country_code
        }

        return Response(data, status=status.HTTP_200_OK)


class SignupAPIView(APIView):
    def post(self, request):
        data = request.data
        message = 'success'

        country_code = data.get('country_code')
        mobile_number = f"{country_code}{data.get('mobile_number')}"

        form = SignupForm({
            'email': data.get('email'),
            'name': data.get('name'),
            'mobile_number': mobile_number,
            'password1': data.get('password1'),
            'password2': data.get('password2'),
            'country_code': country_code
        })

        if form.is_valid():
            user = form.save(commit=False)
            user.country_code = country_code
            user.save()
        else:
            message = form.errors.as_json()
        
        return Response({'message': message}, status=status.HTTP_200_OK)
    
from rest_framework.permissions import AllowAny

class EditProfileAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        user = request.user
        name = request.data.get('name')
        email = request.data.get('email')
        mobile_number = request.data.get('mobile_number')
        country_code = request.data.get('country_code')

        if User.objects.exclude(id=user.id).filter(email=email).exists():
            return Response({'message': 'email already exists'})
        elif User.objects.exclude(id=user.id).filter(mobile_number=mobile_number).exists():
            return Response({'message': 'mobile number already exists'})
        else:
            form = ProfileForm(request.data, instance=user)

            if form.is_valid():
                form.save()
                return Response({'message': 'profile uploaded successfully'})
            else:
                return Response( form.errors, status=400)