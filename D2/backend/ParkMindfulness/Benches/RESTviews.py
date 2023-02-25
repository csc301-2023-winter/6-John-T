from django.http import HttpResponse
from rest_framework.response import Response
from Benches.models import Benches, Park
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from Benches.serializers import BenchCreationSerializer, BenchViewSerializer, BenchUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from django.shortcuts import render


# NOTE: This code was meant to be part of the submission, but given the fact that we had to include a UI
# we were forced to go with the Django forms approach. This code is left here as THIS is the actual code
# that will be used in the project (the API), but given the format of the assignment, it had to be left out.

# from ParkMindfulness.forms import BenchesForm

# Here would go the CRUD API for the bench model to be implemented by Michele

# def index(request):
#     if request.method == 'GET': 
#         form = BenchesForm()
#         context = {'form': form} 
#         return render(request, 'test_page.html', context) # html under templates
#     return HttpResponse("Hello, world. You're at the benches index.") 

# Benches CRUD view:
# Containst the methods for POST(create), GET(read), PUT(update), and DELETE(delete) a bench object 
# from the database

class BenchCreateView(CreateAPIView):

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
        
        # take in the data from the request to create a new bench object
        serializer = BenchCreationSerializer(data=request.data)
        # at the moment, QR code generation not implemented as its not required by the user story yet

        # re-check with the serializer
        if not serializer.is_valid():
            return Response({"message": "Bench creation failed (client error). Make sure to fill out all of the fields!"}, status=400)
        
        # otw
        serializer.save()
        return Response({"message": "Bench object has been created!"}, status=201)
            

# The view to get all the benches in the database corresponding to the given park id
class BenchGetView(ListAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = BenchViewSerializer  # the serializer that shows all the details
    
    def get_queryset(self):
        # fetch the park id from the request kwargs
        park_to_display = self.kwargs['park_id']
        # get all benches in the database with the given park id

        benches = Benches.objects.filter(park_id=park_to_display)
        park = Park.objects.filter(park_id=park_to_display)  
        if benches.exists():
            return benches.order_by('bench_id')
        elif not park.exists():
            # when the entered park does not exist in the database
            raise ParseError({"message": "The park id entered does not exist in the database"})
        else: 
            # the park exists but there are no benches in the database, so return an empty list
            return []
            
        

# The view to update a bench object in the database (can only update the name, qr_code, and thumbnail)
class BenchUpdateView(UpdateAPIView):

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
    

# The view to delete a bench object in the database
class BenchDeleteView(DestroyAPIView):
    
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
        



