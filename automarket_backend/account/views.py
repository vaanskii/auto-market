from rest_framework.decorators import api_view
from .forms import SignupForm
from django.http import JsonResponse
from rest_framework import status

@api_view(['GET'])
def user(request):
    if hasattr(request.user, 'mobile_number'):
        mobile_number = str(request.user.mobile_number)
    else:
        mobile_number = None

    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': getattr(request.user, 'email', None),
        'mobile_number': mobile_number,
    })

@api_view(['POST'])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'mobile_number': data.get('mobile_number'),
        'password1': data.get('password1'),
        'password2': data.get('password2')
    })

    if form.is_valid():
        user = form.save()
        user.save()
        return JsonResponse({'message': message}, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({'message': 'error', 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)