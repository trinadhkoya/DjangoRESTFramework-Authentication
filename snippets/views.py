# Create your views here.
from rest_framework import generics
from rest_framework import mixins

from snippets.models import Snippets
from snippets.serializers import SnippetSerializer

'''

in this everything in terms of class based views  like we weorked with functions

'''


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippets.objects.all();
    serializer_class = SnippetSerializer

    '''
         in this  waht we are doing is getting the data (snippets) and  creating the Snippets
 so we are using list and create mixins and methods as well

    '''

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


'''
# dealing with  update and Delete and Retrieve so
# used corresponding mixins like Retrieve and update and Destroy and methods as well

'''


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippets.objects.all();
    # returns all snippets
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        print request
        print args
        print kwargs

        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
