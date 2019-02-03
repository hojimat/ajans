from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Actor
from .helpers import all_fields

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class ActorForm(forms.ModelForm):
#	image_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}), required=True)
	class Meta:
		model = Actor
		fields = all_fields
		widgets = {'image': forms.ClearableFileInput(attrs={'multiple':True}),
				   'video': forms.ClearableFileInput(attrs={'multiple':True}),
				   'imagedir': forms.HiddenInput(),
				   'videodir': forms.HiddenInput(),
				  }
