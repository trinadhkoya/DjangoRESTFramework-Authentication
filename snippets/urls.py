from django.conf.urls import url
from snippets import views
from snippets.views import SnippetList

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),

    url(r'^snippets/(?P<key>[0-9]+)/$', views.SnippetDetail.as_view()),
]