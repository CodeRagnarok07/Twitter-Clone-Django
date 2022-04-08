from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("bio", "image", "image_header")
