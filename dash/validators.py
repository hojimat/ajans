from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def validate_video(value):
	FileExtensionValidator(allowed_extensions=['mp4', 'webm', 'ogg', 'mov', '3gp', 'avi'])

def validate_day(value):
	pass

def validate_month(value):
	pass

def validate_year(value):
	pass


