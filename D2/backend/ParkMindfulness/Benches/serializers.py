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
        fields = ["audio_binary", "audio_file", "contributor", "length_category", "season_category"]


### The serializer to be used to show to the admins to create the bench
class BenchCreationSerializer(serializers.ModelSerializer):
    secondary_model = BenchCreationAudioSerializer()

    class Meta:
        model = Benches
        # all needed fields but the qr code should be displayed and required
        fields = ["bench_title", "park_id", "thumbnail", "secondary_model"]


### The serializer to be used to actually create the bench object
class FullBenchCreationSerializer(serializers.ModelSerializer):
    secondary_model = FullAudioSerializer()

    class Meta:
        model = Benches
        # all needed fields but the qr code should be displayed and required
        fields = ["bench_title", "park_id", "thumbnail", "secondary_model"]

    def create(self, validated_data):
        """
        Modified to create a bench and its associated audio file
        """
        audio_data = validated_data.pop('secondary_model')
        bench = Benches.objects.create(**validated_data)
        Audio.objects.create(bench_id=bench, **audio_data)
        return bench


#################
# BENCH VIEWING #
#################

### The audio viewing model serializers for both admin and user
class BenchViewAudioSerializer_admin(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ["audio_id", "audio_binary", "audio_file", "contributor", "length_category", "season_category"]

class BenchViewAudioSerializer_user(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ["audio_binary", "audio_file", "contributor"]

class BenchViewSerializer_admin(serializers.ModelSerializer):

    class Meta:
        model = Benches
        fields = ["bench_id", "bench_title", "qr_code", "park_id", "thumbnail"]

class BenchViewSerializer_user(serializers.ModelSerializer):
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
    
    
### The serializer to be used to actually create the bench object (using full audio)
class FullBenchUpdateSerializer(serializers.ModelSerializer):
    secondary_model = FullAudioSerializer()

    class Meta:
        model = Benches
        # all needed fields but the qr code should be displayed and required
        fields = fields = ["bench_title", "thumbnail", "secondary_model"]

    def update(self, instance, validated_data):
        """
        Modified to update a bench and its associated audio file
        """
        audio_data = validated_data.pop('secondary_model')
        audio_instance = Audio.objects.get(bench_id=instance)
        bench_instance = super().update(instance, validated_data)
        
        # update the audio instance by iterating over the dictionary of data passed to us
        # and updating each field 1 by 1. Not the most efficient way, but given the possible
        # empty fields and such, this gets it done
        for column, value in audio_data.items():
            setattr(audio_instance, column, value)
        audio_instance.save()

        return bench_instance
    

#########
# OTHER #
#########
    
class ParkViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ["park_id", "name", "location"]