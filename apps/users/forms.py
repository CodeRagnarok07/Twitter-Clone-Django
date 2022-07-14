from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = [ 'email','password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User

        fields = '__all__'


