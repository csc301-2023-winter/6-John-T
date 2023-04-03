from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Park)
class AdminProfile(admin.ModelAdmin):
    list_display = ['park_id','name', 'location']