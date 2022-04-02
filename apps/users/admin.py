from django.contrib import admin

# Register your models here.

from .models import Profile, Relationship

admin.site.register(Profile)
admin.site.register(Relationship)