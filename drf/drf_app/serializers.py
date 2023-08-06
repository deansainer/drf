from rest_framework.serializers import ModelSerializer
from .models import *


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'