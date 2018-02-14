from . import models
from . import serializers

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
''' class ListPoll(generics.ListCreateAPIView):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer

class DetailPoll(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer '''

def ListPoll(request):
    if request.method == 'GET':
        queryset = models.Poll.objects.all()
        serializer_class = serializers.PollSerializer(queryset, many = True)
        return JsonResponse(serializer_class.data, safe=False)