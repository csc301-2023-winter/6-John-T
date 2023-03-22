# view specific imports
from django.forms import model_to_dict
from rest_framework.response import Response
from Benches.models import Benches, Audio
from .models import Park
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404
from django.conf import settings

# for handling file deletion within /media
import os

# qr code generation imports
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO

#################
# PARK CREATION #
#################

# Park creation views to be implemented by Sam as part of the CRUD API views

################
# PARK VIEWING #
################

# The view to get all Parks in the database
class ParkGetAllView_admin(ListAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = ParkViewSerializer  # the serializer that shows all the details
    
    def get_queryset(self):
        # get all parks in the database
        parks = Park.objects.all()
        print(parks)
        if parks.exists():
            return parks.order_by('park_id')
        else: 
            # the park exists but there are no benches in the database, so return an empty list
            return []
        
        
#################
# PARK UPDATING #
#################

# Park updating views to be implemented by Sam as part of the CRUD API views

#################
# PARK DELETION #
#################

# Park deletion views to be implemented by Sam as part of the CRUD API views
