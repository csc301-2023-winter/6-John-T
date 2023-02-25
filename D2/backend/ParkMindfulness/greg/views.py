from django.shortcuts import render

# Create your views here.
# following https://docs.djangoproject.com/en/4.1/intro/tutorial01/ 
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
