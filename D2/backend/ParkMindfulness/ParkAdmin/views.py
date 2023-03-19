# view specific imports
from rest_framework.response import Response
from .models import CustomAdminUser
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404
from .serializers import UserCreationSerializer

from django.contrib.auth.password_validation import validate_password
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

# keep in mind email == username

CREATION_MESSAGE = "Your email has been added as an administrator for the Park Mindfulness \
application managed by Ontario Parks.\n\nTo finish the setup of your account, please \
go to {} and use the following temporary email and password to log in:\n\
Email: {}\nPassword: {}\n\n"

#################
# USER CREATION #
#################

class NewUserCreateView(CreateAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = UserCreationSerializer
    
    def post(self, request, *args, **kwargs):
        
        # get the email input from the user
        if not request.data['username']:
            return Response({"message": "The email field cannot be empty"}, status=400)
        email = request.data.get('username', None)

        # generate a random password for the user that will be used temporarily until 
        # they finish setting up their account
        password = get_random_string(length=25)

        # send email to the target user with the temporary password so that they can log in
        # and finish setting up their account

        url = "http:/localhost:8000/admin/finish_admin_setup/"

        subject = "Welcome, new admin, to Park Mindfulness!"
        message = CREATION_MESSAGE.format(url, email, password)
        from_email = "ParkMindfulness-Team-6@outlook.com"
        to_email = [email]

        send_mail(subject, message, from_email, to_email, fail_silently=False)

        # create the user with the provided email and other fields once the email is sent
        _ = CustomAdminUser.objects.create_user(username=email, password=password)

        return Response({"message": "The user has been created successfully"}, status=201)


# class FinalizeAdminCreationView(UpdateAPIView):
