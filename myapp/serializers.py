from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    city=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)