from django.contrib import admin
from .models import *

"""
Register the models with the Django admin interface to manage parks. 
"""

@admin.register(Park)
class AdminProfile(admin.ModelAdmin):
    """
    Admin class for Park.
    """
    list_display = ['park_id','name', 'location']