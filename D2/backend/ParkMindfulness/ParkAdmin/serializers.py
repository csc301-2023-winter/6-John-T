from rest_framework import serializers
from .models import CustomAdminUser

# To be implemented by Michele as part of the CRUD API views

#################
# USER CREATION #
#################

### The custom user model creation serializer
class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdminUser
        fields = ["username"] # which really means email

class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdminUser
        fields = "__all__"