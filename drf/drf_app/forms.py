from django.forms import forms, ModelForm
from .models import *


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
