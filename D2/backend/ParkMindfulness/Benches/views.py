# view specific imports
from django.shortcuts import render, redirect
from .forms import BenchesCreateForm, BenchesUpdateForm, BenchesDeleteForm
from rest_framework.response import Response
from .models import Benches, Park
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import BenchCreationSerializer, BenchViewSerializer, BenchUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404

# qr code generation imports
import qrcode
from django.core.files.base import ContentFile
from io import BytesIO


## Merge of RESTviews.py and views.py (to make use of the REST API approach)


##################
# BENCH CREATION #
##################

class BenchCreateView_admin(CreateAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = BenchCreationSerializer
    
    def post(self, request, *args, **kwargs):
        
        # check that the entered park id exists in the database
        park = Park.objects.filter(park_id=request.data['park_id'])
        if not park.exists():
            return Response({"message": "The park id entered does not exist in the database"}, status=400)
        
        # check the bench title and thumbnail fields are not empty
        if not request.data['bench_title']:
            return Response({"message": "The bench title field cannot be empty"}, status=400)
        if not request.data['thumbnail']:
            return Response({"message": "The thumbnail field cannot be empty"}, status=400)
        
        # TODO: add audio file if uploaded by user

        # take in the data from the request to create a new bench object
        serializer = BenchCreationSerializer(data=request.data)

        # save the bench object in the database as is (no qr code yet)
        if not serializer.is_valid():
            return Response({"message": "Bench creation failed (client error). Make sure to fill out all of the fields!"}, status=400)
        # otw
        bench = serializer.save()

        bench_data = serializer.data
        # create the qr code that is to identify this bench object when users scan it

        # build the front end link template that we are to make the QR code for
        qr_link = f"https://6-john-t-one.vercel.app/#/media?m={bench.bench_id}"

        # use the qrcode library to make a qr code image through teh qr_class class
        qr_class = qrcode.QRCode(version=1, box_size=20, border=4)
        qr_class.add_data(qr_link)
        qr_class.make(fit=True)
        # actually create the image
        bench_qr = qr_class.make_image(fill_color="black", back_color="white")
        # save the image to a buffer in PNG format
        buffer = BytesIO()
        bench_qr.save(buffer, format='PNG')
        
        # save the qr code from the buffer to the bench object in the database
        bench.qr_code.save(f"qr_code_{bench.bench_id}.png", ContentFile(buffer.getvalue()), save=True)

        return Response({"message": "Bench object has been created!"}, status=201)


#########################################
# BENCH VIEWING  (park and bench based) #
#########################################

# # simple view for bench viewing (getting all objects)
# def bench_view(request):
#     # get all benches from the DB (filtering and such would be available through our REST API)
#     benches = Benches.objects.all()
#     # render the view with the context variable loaded with all the benches
#     return render(request, 'view.html', {'benches': benches})

# The view to get the bench in the database corresponding to the given bench id
class BenchGetView_admin(RetrieveAPIView):

    # permission_classes = [IsAuthenticated]  -- to be enabled once we have user authentication
    serializer_class = BenchViewSerializer  # the serializer that shows all the details
    
    def get(self, request, *args, **kwargs):
        """
        Contract with frontend: given bench_id, must return:
        - title of bench
        - author of bench  # TODO
        - link to audio file on server  # TODO
        - link to image file on server
        - link to QR code file
        - a boolean that tells you if there is a audio file or not  # TODO
        """
        # fetch the bench id from the request kwargs
        bench_to_display = self.kwargs['bench_id']

        # get the bench in the database with the given bench id or raise a 404 (not found) error
        bench = get_object_or_404(Benches, bench_id=bench_to_display)

        # serialize the bench object
        serializer = BenchViewSerializer(bench)

        # check for audio file in the serialized data
        # serializer.data['audio_file_present'] = True if serializer.data['audio_file'] is not None else False

        return Response(serializer.data)


##################
# BENCH UPDATING #
##################

# The view to update a bench object in the database (can only update the name, audio, author, and thumbnail)
class BenchUpdateView_admin(UpdateAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = BenchUpdateSerializer
    
    def put(self, request, *args, **kwargs):  # behaves like a post request

        # make mutable copy of the request data
        new_data = request.data.copy()

        # otw, fetch the bench id from the request kwargs and get the object from DB
        bench_to_update = self.kwargs['bench_id']  
        bench = Benches.objects.filter(bench_id=bench_to_update).first()

        # determine which fields are to be updated, whichever field has been left empty should not be
        # erased, but rather keep the original value
        if not request.data['bench_title']:
            new_data['bench_title'] = bench.bench_title
        if not request.data['thumbnail']:
            new_data['thumbnail'] = bench.thumbnail
        # if not request.data['audio_file']:
        #     new_data['audio_file'] = bench.audio_file
        # if not request.data['author']:
        #     new_data['author'] = bench.author


        # take in the data from the request to update the bench object
        serializer = self.serializer_class(data=new_data)

        if not serializer.is_valid():
            return Response({"message": "Bench update could not go through (client error)!"}, status=400)

        if bench:
            # then we can update the bench object (the first and only one that should exist) with the given data
            serializer.update(bench, serializer.validated_data)
            return Response({"message": "Bench object has been updated!"}, status=200)
        else:
            # Return not found error message
            return Response({"message": "No bench found for the given bench id"}, status=404)


##################
# BENCH DELETION #
##################

# The view to delete a bench object in the database
class BenchDeleteView_admin(DestroyAPIView):
    
    # permission_classes = [IsAuthenticated]

    # queryset = Benches.objects.all()
    
    def delete(self, request, *args, **kwargs):
        # fetch the bench id from the request kwargs
        bench_to_delete = self.kwargs['bench_id']
        # get the bench object with the given bench id
        bench = Benches.objects.filter(bench_id=bench_to_delete)

        if bench.exists():
            # say bye bye to the bench
            bench.delete()
            return Response({"message": "Bench object has been deleted!"}, status=200)
        else:
            # Return not found error message if no corresponding bench is found
            return Response({"message": "No bench found for the given bench id"}, status=404)