# view specific imports
from rest_framework.response import Response
from .models import CustomAdminUser
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404
from .serializers import *
from Benches.models import Park

from django.contrib.auth.password_validation import validate_password
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from django.middleware.csrf import get_token
from django.contrib.auth.hashers import make_password
from django.conf import settings

# keep in mind email == username
CREATION_MESSAGE = "Your email has been added as an administrator for the Park Mindfulness \
application managed by Ontario Parks.\n\nTo finish the setup of your account, please \
go to {} and use the following temporary email and password to log in:\n\
Username: {}\nPassword: {}\n\nOnce in, you can go onto your account and update your \
password and create the park you manage.\n\n"
STAGING_LOGIN = "https://6-john-t.vercel.app/login"
PROD_LOGIN = "https://parkmindfulness-manager.netlify.app/login"


#########################
# USER CREATION / LOGIN #
#########################

class NewUserCreateView(CreateAPIView):
    """
    API view to create a new user.

    A password is randomly generating and information is sent to user's email.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserCreationSerializer
    
    def post(self, request, *args, **kwargs):
        
        # check that the user is a superuser
        if not request.user.is_superuser:
            return Response({"message": "You are not authorized to create new users"}, status=401)

        # get the email input from the user
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Make sure you have properly setup the fields"}, status=400)
        email = request.data.get('username', None)

        # generate a random password for the user that will be used temporarily until 
        # they finish setting up their account
        password = get_random_string(length=25)

        # send email to the target user with the temporary password so that they can log in
        # and finish setting up their account

        # determine which url to redirect users to for login
        if settings.DEBUG_N == True:
            url = STAGING_LOGIN
        else:
            url = PROD_LOGIN

        subject = "Welcome, new admin, to Park Mindfulness!"
        message = CREATION_MESSAGE.format(url, email, password)
        from_email = "ParkMindfulness-Team-6@outlook.com"
        to_email = [email]

        send_mail(subject, message, from_email, to_email, fail_silently=False)

        # create the user with the provided email and other fields once the email is sent
        _ = CustomAdminUser.objects.create_user(username=email, password=password)

        return Response({"message": "The user has been created successfully"}, status=201)


# LOGIN/LOGOUT functionality is now handled through tokens


###################
# USER MANAGEMENT #
###################

class UpdateAdminInfoView(UpdateAPIView):
    """
    API view to update user's information like passwords. 
    """
    
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateInfoSerializer

    def post(self, request, *args, **kwargs):

        # get the email and password from the user
        if not request.data['username'] or not request.data['old_password']:
            return Response({"message": "The email and old_password fields cannot be empty"}, status=400)
        # have to check manually as serializer checks for uniqueness of username, which it isnt as its for a created account

        email = request.data.get('username', None)
        old_password = request.data.get('old_password', None)
        new_password = request.data.get('new_password', None)
        confirm_password = request.data.get('confirm_password', None)
        manages_park = request.data.get('manages_park', None)

        # check if the user exists
        user = get_object_or_404(CustomAdminUser, username=email)

        # check if the old password is correct before allowing changes to be made
        if not user.check_password(old_password):
            return Response({"message": "The old password is incorrect"}, status=400)

        if old_password and new_password and confirm_password:
            
            # check if the new password and confirm password match
            if new_password != confirm_password:
                return Response({"message": "The new and confirm passwords do not match"}, status=400)
            
            # now you can authenticate the user and update their password

            # validate the password
            try:
                validate_password(new_password)
            except ParseError as e:
                return Response({"message": e.detail}, status=400)

            # if successful, proceed
            user.set_password(new_password)

        if manages_park and old_password:
            # update the park that the user manages

            # get the park object
            park = get_object_or_404(Park, park_id=manages_park)
            
            user.manages_park = park
        

        # save the changes
        user.save()
        return Response({"message": "The user information has been updated"}, status=201)
    

class GetAdminInfoView(RetrieveAPIView):
        """
        API view to retrieve user information.
        """
    
        permission_classes = [IsAuthenticated]
        serializer_class = GetInfoSerializer
    
        def get(self, request, *args, **kwargs):
    
            # get the admin id from the query params
            admin_id = request.user.id

            # check if the user exists
            user = get_object_or_404(CustomAdminUser, id=admin_id)
    
            # return the user information
            validated_data = self.serializer_class(user).data

            return Response(validated_data, status=200)
        

class DeleteAdminView(DestroyAPIView):
    """
    API view to delete a user.
    """
    
    permission_classes = [IsAuthenticated]
    # doesnt really need a serializer

    def delete(self, request, *args, **kwargs):

        # get the admin id from the query params
        admin_id = request.user.id

        if not admin_id:
            return Response({"message": "Please specify an admin Id"}, status=400)
        
        # if the user exists, delete the user
        user = get_object_or_404(CustomAdminUser, id=admin_id)

        user.delete()

        return Response({"message": "The user has been deleted successfully"}, status=200)
