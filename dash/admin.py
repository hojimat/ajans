from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	def get_fields(self, request, obj=None):
		if request.user.is_superuser:
			return ('user', 'bio', "age")
		else:
			if obj.age>5:
				return ('bio',"age")
			return ()

