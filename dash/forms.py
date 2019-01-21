from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'bio')

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

