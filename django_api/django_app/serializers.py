from rest_framework import serializers

class StudentSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=40)
    roll_number = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
