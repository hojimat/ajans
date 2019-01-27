from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Actor

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class ActorForm(ModelForm):
	class Meta:
		model = Actor
		fields = ['ad', 'soyad', 'TCno', 'baba', 'gun', 'ay', 'yil',
				'kayitgun', 'kayitay', 'kayityil',
				'tel1', 'bilgi1', 'tel2', 'bilgi2', 'tel3', 'bilgi3',
				'tel4', 'bilgi4', 'tel5', 'bilgi5',
				'mail', 'adres',

				'imagedir', 'videodir', 'ulke', 'il', 'ilce',
				'bay', 'bayan', 'ucuncucins', 'oryantel',
				'tbay', 'tbayan', 'muzisyen', 'ikiz', 'ybay', 'ybayan',
				'ekstra', 'cuce', 'mbay', 'mbayan', 'elcasti',
				'dovmeli', 'boy', 'kilo', 'beden', 'ayak', 'goz',
				'ozellik', 'pazartesi', 'sali', 'carsamba', 'persembe',
				'cuma', 'cumartesi', 'pazar', 'emekli', 'pasaport',
				'sgk', 'protokol', 'd', 'r', 'df', 'dans', 'solist',
				'ozeltip', 'dublor', 'dublaj', 'engelli', 'gorme',
				'isitme', 'kekeme', 'down', 'sacsekli', 'sacrengi',
				'tenrengi', 'incelendi', 'otizm', 'TCStatus'
				]
