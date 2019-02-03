from .models import Actor
import os

mynumber = str(Actor.objects.all().count() + 1).zfill(10)

def save_image(f):
	with open(os.path.join(f"media/images/{mynumber}", f.name), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def save_video(f):
	with open(os.path.join(f"media/videos/{mynumber}", f.name), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
