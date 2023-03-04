from rest_framework import serializers
from Benches.models import Benches, Audio, Park

# To be implemented by Michele as part of the CRUD API views

# The audio model serializer to be included as part of the bench serializers
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

    def create(self, validated_data):
        """
        Modified to create a bench and its associated audio file
        """
        audio_data = validated_data.pop('secondary_model')
        bench = Benches.objects.create(**validated_data)
        Audio.objects.create(bench_id=bench, **audio_data)
        return bench

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

class BenchViewSerializer_admin(serializers.ModelSerializer):
    class Meta:
        model = Benches
        # all needed fields including the qr code
        fields = "__all__"

class BenchViewSerializer_user(serializers.ModelSerializer):
    class Meta:
        model = Benches
        # all needed fields BUT the qr code and the bench id
        fields = ["bench_title", "thumbnail"]  # TODO: should include author and audio file
        

class BenchUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benches
        fields = ["bench_title", "thumbnail"]  # TODO: should include author and audio file
    
class ParkViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = ["park_id", "name", "location"]