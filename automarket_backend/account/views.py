from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import SignupForm

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