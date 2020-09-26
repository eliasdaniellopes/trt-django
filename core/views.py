from django.shortcuts import render
from rest_framework import viewsets
from .models import Registros_filtrados
from .serializer import RegistroSerializer

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registros_filtrados.objects.all()
    serializer_class = RegistroSerializer
