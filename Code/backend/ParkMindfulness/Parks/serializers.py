from rest_framework import serializers
from Benches.models import Benches, Audio
from Parks.models import Park


#################
# PARK CREATION #
#################

class ParkCreationSerializer(serializers.ModelSerializer):
    """
    Serializer class to create a new park object.
    """
    class Meta:
        model = Park
        fields = ["name", "location"]


################
# PARK VIEWING #
################
    
class ParkViewSerializer(serializers.ModelSerializer):
    """
    Serializer class to retreive park information.
    """
    class Meta:
        model = Park
        fields = ["park_id", "name", "location"]
        
        
#################
# PARK UPDATING #
#################

class ParkUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer class for updating an existing park's information.
    """
    class Meta:
        model = Park
        fields = ["name", "location"]