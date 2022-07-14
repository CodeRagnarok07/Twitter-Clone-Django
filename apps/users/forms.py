from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

<<<<<<< HEAD
# from django.forms import ModelForm
=======
from django.contrib.auth.models import User
from .models import CustomUser
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86


class UserRegisterForm(UserCreationForm):
    class Meta:
<<<<<<< HEAD
        model = User
        fields = ['email', 'username', 'name', 'password1', 'password2']
=======
        model = CustomUser
        fields = '__all__'
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86


class UserUpdateForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model = User
        fields = '__all__'
=======
        model = CustomUser
        fields = '__all__'

>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model = User
        fields = ('bio','img')#['header','bio', 'img']
=======
        model = CustomUser
        fields = ("bio", "image", "image_header")
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86
