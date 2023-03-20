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


################
# LOGIN/LOGOUT #
################

class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = CustomAdminUser
        fields = ["username", "password"]


###################
# USER MANAGEMENT #
###################

class UpdateInfoSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = CustomAdminUser
        fields = UserCreationSerializer.Meta.fields + ["old_password", "new_password", "confirm_password"] + ["manages_park"]

class GetInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAdminUser
        fields = ["id", "username", "manages_park"]