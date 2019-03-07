from django.core.management.base import BaseCommand, CommandError
from django.db import migrations, models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
#from dash.models import Actor, User


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		# Define groups
		g_owner = Group.objects.get_or_create(name='owner')[0]
		g_staff = Group.objects.get_or_create(name='staff')[0]
		g_client = Group.objects.get_or_create(name='client')[0]
