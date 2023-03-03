from rest_framework import serializers
from Benches.models import Benches

# To be implemented by Michele as part of the CRUD API views


class BenchCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benches
        # all needed fields but the qr code should be displayed and required
        fields = ["bench_title", "park_id", "thumbnail"]

class BenchViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benches
        # all needed fields but the qr code should be displayed and required
        fields = "__all__"
        

class BenchUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benches
        fields = ["bench_title", "thumbnail"]  # TODO: should include author and audio file
        