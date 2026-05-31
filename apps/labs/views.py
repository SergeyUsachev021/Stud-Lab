from rest_framework import generics
from .models import Lab
from .serializers import LabSerializer, LabDetailSerializer


class LabListView(generics.ListAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

class LabDetailView(generics.RetrieveAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabDetailSerializer
