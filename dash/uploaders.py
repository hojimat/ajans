import os
def save_image(f):
	with open(os.path.join('media/images', f.name), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
