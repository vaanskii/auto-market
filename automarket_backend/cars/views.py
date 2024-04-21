from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from .forms import ImageModelForm, CarForm
from .serializers import CarSerializer


@api_view(['POST'])
def create_cars(request):
    form = CarForm(request.POST)
    image = None
    image_form = ImageModelForm(request.POST, request.FILES)

    if image_form.is_valid():
        image = image_form.save(commit=False)
        image.created_by = request.user
        image.save()

    if form.is_valid():
        cars = form.save(commit=False)
        cars.created_by = request.user
        cars.save()

        if image:
            cars.images.add(image)

        user = request.user
        user.save()

        serializer = CarSerializer(cars)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add something here later!...'})