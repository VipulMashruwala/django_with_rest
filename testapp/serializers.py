from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city','marks']
        # read_only_fields = ['roll']
        extra_kwargs = {
            'name' : {
                'required': True
            },
            'roll' : {
                'required': True
            },
            'city' : {
                'required' : True
            },
            'marks' : {
                'required' : True
            }
        }


  
    