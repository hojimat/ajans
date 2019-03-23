from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignupForm, ActorForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate, logout
from .models import Actor
from .uploaders import save_image, save_video
from .helpers import public_fields, private_fields
from .filters import ActorFilter
import os

# Create your views here.
def index(request):
    return render(request, 'templates/index.html',)

@login_required(login_url='/giris/')
def catalogue(request):
	actor_list = Actor.objects.all()

	actors = actor_list.values()
	actor_filter = ActorFilter(request.GET, queryset=actor_list)
	return render(request, 'templates/catalogue.html', {'actors':actors, 'filter': actor_filter})

# Custom decorator for groups:
def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='/giris/')

@login_required(login_url='/giris/')
def portfolio_public(request, actorid):
	actor = Actor.objects.filter(id=int(actorid))[0].__dict__
	public_actor = dict((z, actor[z]) for z in public_fields if z in actor).items()
	return render(request, 'templates/portfolio_public.html', {'actor': public_actor})

@login_required(login_url='/giris/')
@group_required('staff', 'owner')
def portfolio_private(request, actorid):
	actor = Actor.objects.filter(id=int(actorid))[0].__dict__
	private_actor = dict((z, actor[z]) for z in private_fields if z in actor).items()
	return render(request, 'templates/portfolio_private.html', {'actor': private_actor})
	


@login_required(login_url='/giris/')
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


@login_required(login_url='/giris/')
@group_required('staff', 'owner')
def add_new_actor(request):
	if request.method == 'POST':
		form = ActorForm(request.POST, request.FILES)
		images = request.FILES.getlist('image')
		videos = request.FILES.getlist('video')
		if form.is_valid():
			actor = form.save(commit=False)

			mynum = str(Actor.objects.all().count() + 1).zfill(10)
			
			user_images_path = f"media/images/{mynum}"
			user_videos_path = f"media/videos/{mynum}"
			actor.imagedir = user_images_path
			actor.videodir = user_videos_path

			if not os.path.isdir(user_images_path):
				os.mkdir(user_images_path)

			if not os.path.isdir(user_videos_path):
				os.mkdir(user_videos_path)

			for img in images:
				save_image(img)

			for vid in videos:
				save_video(vid)

			actor.save()
			return redirect('/katalog')
	else:
		form = ActorForm()
	return render(request, 'templates/add_new_actor.html', {'form':form})
