from django.contrib import admin
from .models import Profile, Role, Identification_type

# Register your models here.
admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Identification_type)