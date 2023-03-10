from rest_framework import serializers
from Benches.models import Benches, Audio, Park

# To be implemented by Michele as part of the CRUD API views


##################
# BENCH CREATION #
##################

### The audio model serializer to be included as part of the bench serializers
class BenchCreationAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ["audio_file", "contributor", "length_category", "season_category"]

class FullAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        # all except the bench id
        # fields = ["audio_binary", "audio_file", "contributor", "length_category", "season_category"]
        fields = "__all__"


### The serializer to be used to show to the admins to create the bench
class BenchCreationSerializer(serializers.ModelSerializer):
    secondary_model = BenchCreationAudioSerializer()

    class Meta:
        model = Benches
        # all needed fields but the qr code should be displayed and required
        fields = ["bench_title", "park_id", "thumbnail", "secondary_model"]


### The serializer to be used to actually create the bench object
class NoAudioBenchCreationSerializer(serializers.ModelSerializer):
    # secondary_model = FullAudioSerializer()

    class Meta:
        model = Benches
        # all needed fields but the qr code should be displayed and required
        fields = ["bench_title", "park_id", "thumbnail"]


#################
# BENCH VIEWING #
#################

### The audio viewing model serializers for both admin and user
class BenchViewAudioSerializer_admin(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ["audio_id", "audio_binary", "audio_file", "contributor", "length_category", "season_category"]
        # fields = "__all__"

class BenchViewAudioSerializer_user(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ["audio_binary", "audio_file", "contributor"]

class BenchViewSerializer_admin(serializers.ModelSerializer):

    class Meta:
        model = Benches
        fields = ["bench_id", "bench_title", "qr_code", "park_id", "thumbnail"]

class BasicBenchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benches
        # all needed fields BUT the qr code and the bench id
        fields = ["bench_title", "thumbnail"]
        

##################
# BENCH UPDATING #
##################

# similar to the bench creation serializer
class BenchUpdateSerializer(serializers.ModelSerializer):
    secondary_model = BenchCreationAudioSerializer()

    class Meta:
        model = Benches
        fields = ["bench_title", "thumbnail", "secondary_model"]
        # fields = ["bench_title", "thumbnail"]
    

#########
# OTHER #
#########
    
class ParkViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ["park_id", "name", "location"]