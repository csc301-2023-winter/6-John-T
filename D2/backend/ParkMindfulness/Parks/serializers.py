from rest_framework import serializers
from Benches.models import Benches, Audio
from Parks.models import Park


#################
# PARK CREATION #
#################

# Park creation serializers to be implemented by Sam as part of the CRUD API views

################
# PARK VIEWING #
################

# Taken over from D2's Benches/serializers.py
    
class ParkViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ["park_id", "name", "location"]
        
        
#################
# PARK UPDATING #
#################

# Park updating serializers to be implemented by Sam as part of the CRUD API views
