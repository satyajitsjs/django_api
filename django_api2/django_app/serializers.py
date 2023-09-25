from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=10)

    def create(self , validate_data):
        return User.objects.create(**validate_data)