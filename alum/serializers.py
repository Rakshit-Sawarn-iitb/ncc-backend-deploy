from rest_framework import serializers
from .models import alum

class alumSerializer(serializers.ModelSerializer):
    class Meta:
        model = alum
        fields = ['firstName', 'lastName', 'mobile', 'email', 'address', 'gender', 'joiningDate', 'passingDate', 'achievments', 'present', 'branch', 'employment', 'domain', 'work']
        