from django.contrib import admin
from .models import *

"""
Register the models with the Django admin interface to manage benches. 
"""

@admin.register(CustomAdminUser)
class AdminProfile(admin.ModelAdmin):
    """
    Admin class for CustomAdminUser.
    """
    list_display = ['id', 'username', 'email', 'manages_park']
