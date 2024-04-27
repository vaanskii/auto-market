from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render


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


def activateEmail(request):
    email = request.GET.get('email', '')
    id = request.GET.get('id', '')

    if email and id:
        user = User.objects.get(id=id, email=email)
        user.is_active = True
        user.save()

        return render(request, 'account_activate.html', {'login_url': 'http://localhost:5173/en/login'})
    else:
        return render(request, 'account_failed.html')

class SignupAPIView(APIView):
    permission_classes = [~IsAuthenticatedOrReadOnly]
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
            user = form.save()
            user.is_active = False
            user.save()

            activation_url = f'{settings.WEBSITE_URL}/activateEmail/?email={user.email}&id={user.id}'
            email_content = f"""
                    <div style="text-align: center;">
                        <p style="font-size: 16px;">Thank you for signing up! Please click the button below to activate your account:</p>
                        <a href="{activation_url}" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; font-size: 14px;">Activate Account</a>
                    </div>
                """


            send_mail(
                "Please verify your email",
                "",
                settings.EMAIL_HOST_USER,
                [user.email],
                html_message=email_content,
                fail_silently=False,
            )
        else:
            message = form.errors.as_json()

        return Response({'message': message}, status=status.HTTP_200_OK)
    

class EditProfileAPIView(APIView):
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
            
class PasswordChangeAPIView(APIView):
    def post(self, request):
        user = request.user
        form = PasswordChangeForm(data=request.data, user=user)

        if form.is_valid():
            form.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': form.errors}, status=404)