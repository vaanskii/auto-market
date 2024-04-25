from rest_framework import serializers

class VinDataSerializer(serializers.Serializer):
    Make = serializers.CharField(max_length=100, required=False)
    Manufacturer_Name = serializers.CharField(max_length=100, required=False)
    Model = serializers.CharField(max_length=100, required=False)
    Model_Year = serializers.CharField(max_length=100, required=False)
    Plant_City = serializers.CharField(max_length=100, required=False)
    Series = serializers.CharField(max_length=100, required=False)
    Trim = serializers.CharField(max_length=100, required=False)
    Vehicle_Type = serializers.CharField(max_length=100, required=False)
    Plant_Country = serializers.CharField(max_length=100, required=False)
    Body_Class = serializers.CharField(max_length=100, required=False)
    Doors = serializers.CharField(max_length=100, required=False)
    Gross_Vehicle_Weight_Rating_From = serializers.CharField(max_length=100, required=False)
    Engine_Number_of_Cylinders = serializers.CharField(max_length=100, required=False)
    Fuel_Type = serializers.CharField(max_length=100, required=False)
    Turbo = serializers.CharField(max_length=100, required=False)
