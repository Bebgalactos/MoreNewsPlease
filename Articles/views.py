from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Article, Newspaper
from .serializers import ArticleSerializer, NewspaperSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ['get', 'head', 'options', 'patch', 'delete']

class NewspaperViewset(viewsets.ModelViewSet):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action == "create_article":
            return ArticleSerializer
        return self.serializer_class

    @action(methods=['post'], detail=True, url_path="create-article")
    def create_article(self, request, pk):
        print("tesr")
        newspaper = get_object_or_404(Newspaper, pk = pk)
        article_serializer = self.get_serializer_class()(data=request.data)
        if article_serializer.is_valid():
            article_serializer.save(newspaper=newspaper)
            return Response(article_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
