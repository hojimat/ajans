from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignupForm, ActorForm
from django.contrib.auth.models import Group
from .models import Actor

# Create your views here.
def index(request):
    return render(request, 'templates/index.html',)

def catalogue(request):
	actors = Actor.objects.all().values()
	return render(request, 'templates/catalogue.html', {'actors':actors})

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name="client"))
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            return redirect('/register/success', {'user':user})
    else:
        form = SignupForm()

    return render(request, 'templates/register_user.html', {'form':form})

def register_success(request):
	user = request.user
	return render(request, 'templates/register_success.html', {"user":user})


def add_new_actor(request):
	if request.method == 'POST':
		form = ActorForm(request.POST, request.FILES)
		if form.is_valid():
			actor = form.save()
			actor.refresh_from_db()
			actor.save()
			return redirect('/katalog')
	else:
		form = ActorForm()
	return render(request, 'templates/add_new_actor.html', {'form':form})
