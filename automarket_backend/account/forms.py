from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User

class SignupForm(UserCreationForm):
    country_code = forms.CharField(max_length=10, required=False)
    class Meta:
        model = User
        fields = ('email', 'name', 'mobile_number', 'password1', 'password2', 'country_code')

class ProfileForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ('name', 'email', 'mobile_number')