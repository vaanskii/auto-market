from rest_framework import serializers

class VinDataSerializer(serializers.Serializer):
    Make = serializers.CharField(max_length=100, required=False, allow_null=True)
    Manufacturer_Name = serializers.CharField(max_length=100, required=False, allow_null=True)
    Model = serializers.CharField(max_length=100, required=False, allow_null=True)
    Model_Year = serializers.CharField(max_length=100, required=False, allow_null=True)
    Plant_City = serializers.CharField(max_length=100, required=False, allow_null=True)
    Series = serializers.CharField(max_length=100, required=False, allow_null=True)
    Trim = serializers.CharField(max_length=100, required=False, allow_null=True)
    Vehicle_Type = serializers.CharField(max_length=100, required=False, allow_null=True)
    Plant_Country = serializers.CharField(max_length=100, required=False, allow_null=True)
    Body_Class = serializers.CharField(max_length=100, required=False, allow_null=True)
    Doors = serializers.CharField(max_length=100, required=False, allow_null=True)
    Gross_Vehicle_Weight_Rating_From = serializers.CharField(max_length=100, required=False, allow_null=True)
    Engine_Number_of_Cylinders = serializers.CharField(max_length=100, required=False, allow_null=True)
    Fuel_Type = serializers.CharField(max_length=100, required=False, allow_null=True)
    Turbo = serializers.CharField(max_length=100, required=False, allow_null=True)

