from rest_framework.decorators import api_view, authentication_classes, permission_classes
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
        'email': getattr(request.user),
        'mobile_number': mobile_number,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    # Extract country code and mobile number from the request
    country_code = data.get('country_code')
    mobile_number = f"{country_code}{data.get('mobile_number')}"

    # Create the form with the extracted country code and mobile number
    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'mobile_number': mobile_number,
        'password1': data.get('password1'),
        'password2': data.get('password2')
    })

    if form.is_valid():
        user = form.save(commit=False)
        user.country_code = country_code
        user.save()
    else:
        message = form.errors.as_json()
    
    return JsonResponse({'message': message}, safe=False)

