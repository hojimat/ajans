from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignupForm, ActorForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate, logout
from .models import Actor

# Create your views here.
def index(request):
    return render(request, 'templates/index.html',)



@login_required(login_url='/login/')
def catalogue(request):
	actors = Actor.objects.all().values()
	return render(request, 'templates/catalogue.html', {'actors':actors})

# Custom decorator for groups:
def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='/login/')



@login_required(login_url='/login/')
@group_required('staff', 'owner')
def register(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user.groups.add(Group.objects.get(name="client"))
			new_user.refresh_from_db()
			new_user.save()
			raw_password = form.cleaned_data.get('password1')
			return render(request, 'templates/register_success.html', {"new_user": new_user})
	else:
		form = SignupForm()

	return render(request, 'templates/register_user.html', {'form':form})


@login_required(login_url='/login/')
@group_required('staff', 'owner')
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
