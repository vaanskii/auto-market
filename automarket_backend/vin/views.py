from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

import requests
from .serializers import VinDataSerializer


class VinDecoderView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        vin = request.query_params.get('vin')
        if vin:
            url = f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()['Results']

                vin_data = {}

                relevant_fields = {
                    'Make': None,
                    'Manufacturer Name': None,
                    'Model': None,
                    'Model Year': None,
                    'Plant City': None,
                    'Series': None,
                    'Trim': None,
                    'Vehicle Type': None,
                    'Plant Country': None,
                    'Body Class': None,
                    'Doors': None,
                    'Gross Vehicle Weight Rating From': None,
                    'Engine Number of Cylinders': None,
                    'Fuel Type': None,
                    'Turbo': None
                }

                for d in data:
                    if d['Variable'] in relevant_fields:
                        vin_data[d['Variable'].replace(' ', '_')] = d['Value']

                serializer = VinDataSerializer(data=vin_data)

                if serializer.is_valid():
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "No data found for the VIN provided."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "VIN is required."}, status=status.HTTP_400_BAD_REQUEST)

