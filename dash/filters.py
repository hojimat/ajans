from .models import Actor
import django_filters
from .helpers import public_fields, private_fields

class ActorFilter(django_filters.FilterSet):
	class Meta:
		model = Actor
		fields = public_fields
