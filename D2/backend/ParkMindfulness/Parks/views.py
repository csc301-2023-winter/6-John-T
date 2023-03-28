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

class ParkCreateView_admin(CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ParkCreationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Create a new park object with validated data
            park = serializer.save()
            return Response({"message": "Park has been created!", "park_id": park.park_id}, status=201)
        else:
            return Response({"message": "Park couldn't be created."}, status=400)

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

class ParkUpdateView_admin(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ParkUpdateSerializer

    def put(self, request, *args, **kwargs): 
        # otw, fetch the park id from the request kwargs and get the object from DB
        park_to_update = self.kwargs['park_id']  
        park = get_object_or_404(Park, park_id=park_to_update)

        # get the existing data for the park object
        park_data = {
            'name': request.data.get('name', None),
            'location': request.data.get('location', None),
        }

        # determine which fields are to be updated, whichever field has been left empty should not be
        # erased, but rather keep the original value
        if not request.data['name']:
            park_data['name'] = park.name
        if not request.data['location']:
            park_data['location'] = park.location

        # create a serializer with the updated data
        serializer = self.get_serializer(park, data=park_data, partial=True)

        if serializer.is_valid():
            # then we can update the park object with validated data
            serializer.save()
            return Response({"message": "Park object has been updated!"}, status=200)
        else:
            return Response({"message": "Park update couldn't go through."}, status=404)

#################
# PARK DELETION #
#################

# Park deletion views to be implemented by Sam as part of the CRUD API views
class ParkDeleteView_admin(DestroyAPIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        # fetch the park id from the request kwargs
        park_to_delete = self.kwargs['park_id']

        # get the park object with the given park id
        park = Park.objects.filter(park_id=park_to_delete)

        # get all benches associated with a park id 
        benches = Benches.objects.filter(park_id=park_to_delete)
        if park.exists():
            # follow procedure from Benches/views.py BenchDeleteView_admin
            # delete all files contained within benches 
            for bench in benches:
                bench_thumbnail = bench.thumbnail
                bench_qr = bench.qr_code
                audio = Audio.objects.filter(bench_id=bench.bench_id)

                thumbnail_path = os.path.join(settings.MEDIA_ROOT, bench_thumbnail.name)

                if os.path.exists(thumbnail_path):
                    os.remove(thumbnail_path)
                qr_path = os.path.join(settings.MEDIA_ROOT, bench_qr.name)
                if os.path.exists(qr_path):
                    os.remove(qr_path)
                
                # delete audio tied to bench 
                if audio.exists():
                    audio = get_object_or_404(Audio, bench_id=bench.bench_id)
                    audio_file = audio.audio_file
                    audio_path = os.path.join(settings.MEDIA_ROOT, audio_file.name)
                    if os.path.exists(audio_path):
                        os.remove(audio_path)

                # delete bench and audio objects 
                audio.delete()
                bench.delete()

            # finally, say bye bye to the park object
            park.delete()
            return Response({"message": "Park and associated benches have been deleted!"}, status=200)
        else:
            # Return not found error message if no corresponding park is found
            return Response({"message": "No park found for the given park id"}, status=404)
