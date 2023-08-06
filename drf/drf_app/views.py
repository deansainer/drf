from django.shortcuts import render, redirect
from rest_framework import generics
import requests
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .forms import *
from .models import *
from .serializers import *


def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PersonForm()

    response = requests.get('http://127.0.0.1:8000/api/persons/').json()
    context = {'response': response, 'form': form}
    return render(request, 'drf_app/index.html', context)


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

# class PersonAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer