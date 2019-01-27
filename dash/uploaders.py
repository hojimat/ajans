from .models import Actor
import os

def save_image(f):
	with open(os.path.join(f"media/images/{Actor.objects.all().last().id + 1}", f.name), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
