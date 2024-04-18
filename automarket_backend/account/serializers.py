from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(max_length=5)
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'mobile_number', 'country_code')