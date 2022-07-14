from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('bio','img')#['header','bio', 'img']
