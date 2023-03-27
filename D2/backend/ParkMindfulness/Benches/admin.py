from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Benches)
class AdminProfile(admin.ModelAdmin):
    list_display = ['bench_id','bench_title', 'park_id', 'qr_code', 'thumbnail']

@admin.register(Audio)
class AdminProfile(admin.ModelAdmin):
    list_display = ['audio_id','bench_id', 'audio_binary', 'audio_file',
                    'contributor', 'length_category', 'season_category']
    list_filter = ('bench_id', 'length_category', 'season_category') # allow filtering by bench id, length, season


    