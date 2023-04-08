from rest_framework import serializers
from Benches.models import Benches, Audio
from Parks.models import Park

##################
# BENCH CREATION #
##################

class BenchCreationAudioSerializer(serializers.ModelSerializer):
    """
    The audio model serializer to be included as part of the bench serializers.

    When creating a new bench, the audio fields that are included are
    audio file, contributor name, length category, and season category.
    """
    class Meta:
        model = Audio
        fields = ["audio_file", "contributor", "length_category", "season_category"]

class FullAudioSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Audio model to display all Audio fields.
    """
    class Meta:
        model = Audio
        fields = "__all__"

class BenchCreationSerializer(serializers.ModelSerializer):
    """
    Serializer class that's used to show admins when creating a bench.    
    """
    secondary_model = BenchCreationAudioSerializer()

    class Meta:
        model = Benches
        fields = ["bench_title", "park_id", "thumbnail", "secondary_model"]

class NoAudioBenchCreationSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Benches model used to create the bench object without audio.
    """
    class Meta:
        model = Benches
        fields = ["bench_title", "park_id", "thumbnail"]


#################
# BENCH VIEWING #
#################

class BenchViewAudioSerializer_admin(serializers.ModelSerializer):
    """
    Serializer class to display audio information for admins.
    """
    class Meta:
        model = Audio
        fields = ["audio_id", "audio_binary", "audio_file", "contributor", "length_category", "season_category"]

class BenchViewAudioSerializer_user(serializers.ModelSerializer):
    """
    Serializer class to display audio information for users.
    """
    class Meta:
        model = Audio
        fields = ["audio_binary", "audio_file", "contributor"]

class BenchViewSerializer_admin(serializers.ModelSerializer):
    """
    Serializer class to display bench information for admins.
    """
    class Meta:
        model = Benches
        fields = ["bench_id", "bench_title", "qr_code", "park_id", "thumbnail"]

class BasicBenchSerializer(serializers.ModelSerializer):
    """
    Serializer class to display basic bench information.

    Fields include the bench title and thumbnail image.
    """
    class Meta:
        model = Benches
        fields = ["bench_title", "thumbnail"]
        

##################
# BENCH UPDATING #
##################

class BenchUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer class used to update existing benches.
    """
    secondary_model = BenchCreationAudioSerializer()

    class Meta:
        model = Benches
        fields = ["bench_title", "thumbnail", "secondary_model"]    