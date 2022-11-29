from .models import Main
from .serializers import MainSerializer
from rest_framework import generics


class MainCreate(generics.ListCreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer