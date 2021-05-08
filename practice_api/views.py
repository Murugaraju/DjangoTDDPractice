from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import DogModelSerializer
from .models import Dog



class DogModelViewSet(ModelViewSet):

    queryset=Dog.objects.all()
    serializer_class=DogModelSerializer
    
