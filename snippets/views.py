from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippets
from snippets.serializers import SnippetSerializer

'''

in this everything in terms of class based views  like we weorked with functions

'''


class SnippetList(APIView):
    '''
    Listing all snippets or creating a new one
    '''

    def get(self, request, format=None):
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class SnippetDetail(APIView):

    def get_object(self,key):
        try:
            return Snippets.objects.get(key)
        except Snippets.DoesNotExist:
            raise Http404

    def get(self,request,key,format=None):

        snippet=self.get_object(key)
        serializer=SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self,request,key,format=None):

        snippet=self.get_object(key)
        serializer=SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,key,format=None):

        snippet=self.get_object(key)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



