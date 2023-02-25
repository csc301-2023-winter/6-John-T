from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Benches)
class AdminProfile(admin.ModelAdmin):
    list_display = ['bench_id','bench_title', 'park_id', 'qr_code', 'thumbnail']

@admin.register(Park)
class AdminProfile(admin.ModelAdmin):
    list_display = ['park_id','name', 'location']