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

# class FullUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomAdminUser
#         fields = "__all__"

class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = CustomAdminUser
        fields = ["username", "password"]

class SetupFinishSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = CustomAdminUser
        fields = UserCreationSerializer.Meta.fields + ["old_password", "new_password", "confirm_password"]


# class SetupFinishSerializer_out(serializers.ModelSerializer):
#     class Meta:
#         model = CustomAdminUser
#         fields = ["password, manages_park"]