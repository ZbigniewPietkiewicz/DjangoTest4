from rest_framework import generics

from . import models
from . import serializers

# Create your views here.
class ListPoll(generics.ListCreateAPIView):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer

class DetailPoll(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer