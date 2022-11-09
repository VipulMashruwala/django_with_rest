from rest_framework import serializers
from .models import Student


def check_city(value):
    city_list = ['Bihar', 'Goa', 'Vadodara', 'Mumbai', 'Shirpur', 'Delhi','Pune','Surat','Burhanpur']
    if value not in city_list:
        raise serializers.ValidationError('check entered city')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 20)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 20, validators = [check_city])
    marks = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.marks = validated_data.get('marks',instance.marks)
        instance.save()
        return instance

    ### Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    def validate(self, data):
        marks = data.get('marks')
        if marks < 33:
            raise serializers.ValidationError("only pass student data can be inserted")
        return data

    