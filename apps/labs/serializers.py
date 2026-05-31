from rest_framework import serializers
from .models import Lab

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = ['id', 'name', 'description', 'year', 'university', 'faculty', 'type_work', 'author', 'downloaded_times']

class LabDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'