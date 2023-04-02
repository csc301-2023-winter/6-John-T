from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CustomAdminUser)
class AdminProfile(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'manages_park']
