from django.contrib import admin
from .models import *

"""
Register the models with the Django admin interface to manage benches. 
"""

@admin.register(Benches)
class AdminProfile(admin.ModelAdmin):
    """
    Admin class for Benches.
    """
    list_display = ['bench_id','bench_title', 'park_id', 'qr_code', 'thumbnail']

@admin.register(Audio)
class AdminProfile(admin.ModelAdmin):
    """
    Admin class for Audio.
    """
    list_display = ['audio_id','bench_id', 'audio_binary', 'audio_file',
                    'contributor', 'length_category', 'season_category']
    list_filter = ('bench_id', 'length_category', 'season_category') 
    """
    Filters for `Audio` in the Django admin interface.
    
    - bench_id: Filter audio by `Bench` object.
    - length_category: Filter audio by the length category.
    - season_category: Filter audio by the season category.
    """


    