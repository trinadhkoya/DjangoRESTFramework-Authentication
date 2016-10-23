from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from snippets.models import Snippets
from snippets.serializers import SnippetSerializer



'''

The dramatic change in the code we have written earlier and in this is ->Request and Response .
Django Rest provided us inbuilt Response and Request object to make it easier for fetching objects


and the @api_view and API_View

status modules and thier codes refractored to normal english code like instead 404,
'''


@api_view(['GET','POST','DELETE'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT',])
def snippet_detail(request, key):
    try:
        snippet = Snippets.objects.get(pk=key)
    except Snippets.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    '''
    here we are returning snippet object with the given value like /1 or /2 /3
    if the data not found it will throw an exception

    '''

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete();
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
