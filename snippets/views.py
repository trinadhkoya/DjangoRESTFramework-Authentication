# Create your views here.
from django.template.context_processors import csrf
from rest_framework import generics
from rest_framework import mixins

from snippets.models import Snippets
from snippets.serializers import SnippetSerializer
'''
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippets.objects.all();
    serializer_class = SnippetSerializer


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippets.objects.all();
    serializer_class = SnippetSerializer

'''

'''
The minor change you can see from

'''
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippets.objects.all();
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer
