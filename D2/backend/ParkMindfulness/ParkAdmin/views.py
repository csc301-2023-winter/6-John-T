# view specific imports
from rest_framework.response import Response
from .models import CustomAdminUser
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404
from .serializers import *

from django.contrib.auth.password_validation import validate_password
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login

# keep in mind email == username

CREATION_MESSAGE = "Your email has been added as an administrator for the Park Mindfulness \
application managed by Ontario Parks.\n\nTo finish the setup of your account, please \
go to {} and use the following temporary email and password to log in:\n\
Username: {}\nPassword: {}\n\n"


#########################
# USER CREATION / LOGIN #
#########################

class NewUserCreateView(CreateAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = UserCreationSerializer
    
    def post(self, request, *args, **kwargs):
        
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

        url = "http://127.0.0.1:8000/park_admin/finish_admin_setup/"

        subject = "Welcome, new admin, to Park Mindfulness!"
        message = CREATION_MESSAGE.format(url, email, password)
        from_email = "ParkMindfulness-Team-6@outlook.com"
        to_email = [email]

        send_mail(subject, message, from_email, to_email, fail_silently=False)

        # create the user with the provided email and other fields once the email is sent
        _ = CustomAdminUser.objects.create_user(username=email, password=password)

        return Response({"message": "The user has been created successfully"}, status=201)


class FinishAdminSetupView(UpdateAPIView):
    
    # permission_classes = [IsAuthenticated]
    serializer_class = SetupFinishSerializer

    def post(self, request, *args, **kwargs):

        # get the email and password from the user
        if not request.data['username']:
            return Response({"message": "The email field cannot be empty"}, status=400)
        if not request.data['old_password'] or not request.data['new_password'] or not request.data['confirm_password']:
            return Response({"message": "The password fields cannot be empty"}, status=400)
        # have to check manually as serializer checks for uniqueness of username, which it isnt as its for a created account

        email = request.data.get('username', None)
        old_password = request.data.get('old_password', None)
        new_password = request.data.get('new_password', None)
        confirm_password = request.data.get('confirm_password', None)

        # check if the user exists
        user = get_object_or_404(CustomAdminUser, username=email)
        # check if the old password is correct
        if not user.check_password(old_password):
            return Response({"message": "The old password is incorrect"}, status=400)
        
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
        user.save()

        user = authenticate(username=email, password=new_password)
        login(request, user)

        return Response({"message": "The user password has been set successfully"}, status=201)


class AdminLoginView(GenericAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):

        # get the email and password from the user
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Make sure you have properly setup the fields"}, status=400)

        email = request.data.get('username', None)
        password = request.data.get('password', None)

        print(email, password)

        user = get_object_or_404(CustomAdminUser, username=email)
        # check if the password is correct
        if not user.check_password(password):
            return Response({"message": "Invalid username-password combination"}, status=400)

        # if successful, authenticate the user
        user = authenticate(username=email, password=password)
        login(request, user)

        return Response({"message": "The user has been logged in successfully"}, status=200)
