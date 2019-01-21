"""sitem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auths
from dash import views as dashs
from django.contrib.staticfiles.urls import staticfiles_urlpatterns as statics

urlpatterns = [

    #system config
    url(r'^admin/', admin.site.urls),
    
    #dashboard
    url(r'^dash/dash-noob/$', dashs.dash_noob),
    url(r'^dash/dash-profi/$', dashs.dash_profi),
    url(r'^dash/dash-owner/$', dashs.dash_owner),
    url(r'^dash/dash-admin/$', dashs.dash_admin),
    url(r'^dash/$', dashs.index),

    #authentication:
    url(r'^dash/register-noob/$', dashs.register_noob),
    url(r'^dash/register-profi/$', dashs.register_profi),
    url(r'^dash/register-owner/$', dashs.register_owner),
    url(r'^dash/login-noob/$', auths.LoginView.as_view(template_name='registration/login_noob.html')),
    url(r'^dash/login-profi/$', auths.LoginView.as_view(template_name='registration/login_profi.html')),
    url(r'^dash/login-owner/$', auths.LoginView.as_view(template_name='registration/login_owner.html')),
    url(r'^dash/login-admin/$', auths.LoginView.as_view(template_name='registration/login_admin.html')),
    url(r'^dash/logout/$', auths.LogoutView.as_view()),
    url(r'^dash/password-reset/$', dashs.password_reset),
]

urlpatterns += statics()
