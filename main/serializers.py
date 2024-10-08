from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
  class Meta:
        model = Student 
        fields = ('pk', 'name', 'email', 'document', 'phone', 'registration_date')