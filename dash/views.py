from django.shortcuts import render

from .forms import SignupForm
from .models import Message, Notification
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

# Main homepage here:
def index(request):
    return render(request, 'templates/dashboard/dash_index.html')


# Custom decorator for groups:
def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='/dash/')







@login_required(login_url='/dash/login-noob/')
@group_required('noob')
def dash_noob(request):
    userr = request.user
    msg = Message.objects.filter(user_id=userr.id)
    ntf = Notification.objects.filter(user_id=userr.id)
    return render(request, 'templates/dashboard/dash_noob.html', {"userr":userr, "msg":msg, "ntf":ntf})

@login_required(login_url='/dash/login-profi/')
@group_required('profi')
def dash_profi(request):
    userr = request.user
    msg = Message.objects.filter(user_id=userr.id)
    ntf = Notification.objects.filter(user_id=userr.id)
    return render(request, 'templates/dashboard/dash_profi.html', {"userr":userr, "msg":msg, "ntf":ntf})

@login_required(login_url='/dash/login-owner/')
@group_required('owner')
def dash_owner(request):
    userr = request.user
    msg = Message.objects.filter(user_id=userr.id)
    ntf = Notification.objects.filter(user_id=userr.id)
    return render(request, 'templates/dashboard/dash_owner.html', {"userr":userr, "msg":msg, "ntf":ntf})

@login_required(login_url='/dash/login-admin/')
@group_required('admin')
def dash_admin(request):
    userr = request.user
    msg = Message.objects.filter(user_id=userr.id)
    ntf = Notification.objects.filter(user_id=userr.id)
    return render(request, 'templates/dashboard/dash_admin.html', {"userr":userr, "msg":msg, "ntf":ntf})



# Authentication here.
def register_noob(request):
    registered = False
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name="noob"))
            user.refresh_from_db()
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            registered = True
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password = raw_password)
            login(request, user)
            return redirect('/dash/dash-noob', {'registered':registered})
    else:
        form = SignupForm()

    return render(request, 'registration/register_noob.html', {'form':form})


def register_profi(request):
    registered = False
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name="profi"))
            user.refresh_from_db()
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            registered = True
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password = raw_password)
            login(request, user)
            return redirect('/dash/dash-profi', {'registered':registered})
    else:
        form = SignupForm()

    return render(request, 'registration/register_profi.html', {'form':form})



def register_owner(request):
    registered = False
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name="owner"))
            user.refresh_from_db()
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            registered = True
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password = raw_password)
            login(request, user)
            return redirect('/dash/dash-owner', {'registered':registered})
    else:
        form = SignupForm()

    return render(request, 'registration/register_owner.html', {'form':form})


def password_reset(request):
    return render(request, 'registration/password_reset.html')
# Create your views here.
