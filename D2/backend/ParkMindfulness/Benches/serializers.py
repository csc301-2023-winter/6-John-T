from rest_framework import serializers
from Benches.models import Benches

# To be implemented by Michele as part of the CRUD API views


class BenchCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benches
        # all needed fields but the qr code should be displayed and required
        fields = ["bench_title", "park_id", "thumbnail"]

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
        