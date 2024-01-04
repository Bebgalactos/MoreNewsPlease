from rest_framework import generics, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Article, Newspaper
from Interactions.models import Interaction
from .serializers import ArticleSerializer, NewspaperSerializer
from django.shortcuts import get_object_or_404
from Interactions.serializers import ReadSerializer , RatingInteractionSerializer , FavoriteInteractionSerializer , ShareInteractionSerializer ,OpinionSerializer
# Create your views here.


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ['get', 'post','head', 'options', 'patch', 'delete']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "read_article":
            return ReadSerializer
        if self.action == "opinion_article":
            return OpinionSerializer
        if self.action == "share_article":
            return ShareInteractionSerializer
        if self.action == "rate_article":
            return RatingInteractionSerializer
        if self.action == "favorite_article":
            return FavoriteInteractionSerializer
        return self.serializer_class
    
    def get_queryset(self):
        if self.action == "read_article":
            return Interaction.objects.all()
        if self.action == "opinion_article":
            return Interaction.objects.all()
        if self.action == "share_article":
            return Interaction.objects.all()
        if self.action == "rate_article":
            return Interaction.objects.all()
        if self.action == "favorite_article":
            return Interaction.objects.all()
        return self.queryset
    
    @action(methods=['post'], detail=True, url_path="read")
    def read_article(self, request : Request, pk):
        user = request.user
        article = get_object_or_404(Article, pk = pk)
        data = {'article' : article.pk , 'user' : user.pk}
        interaction_serializer = ReadSerializer(data=data)
        if interaction_serializer.is_valid():
            interaction_serializer.save(article = article, user = user)
            return Response(interaction_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(interaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['post'], detail=True, url_path="opinion")
    def opinion_article(self, request : Request, pk):
        user = request.user
        article = get_object_or_404(Article, pk = pk)
        data = {'article' : article.pk , 'user' : user.pk, **request.data}
        interaction_serializer = self.get_serializer_class()(data=data)
        previous_rating = self.get_queryset().filter(user = user.pk , article = article.pk , interaction_type = "opinion")
        if len(previous_rating) > 0:
            previous_rating.delete()
        if interaction_serializer.is_valid():
            interaction_serializer.save(article = article, user = user)
            return Response(interaction_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(interaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    @action(methods=['post'], detail=True, url_path="rate")
    def rate_article(self, request : Request, pk):
        user = request.user
        article = get_object_or_404(Article, pk = pk)
        data = {'article' : article.pk , 'user' : user.pk, **request.data}
        interaction_serializer = self.get_serializer_class()(data=data)
        previous_rating = self.get_queryset().filter(user = user.pk , article = article.pk , interaction_type = "rating")
        if len(previous_rating) > 0:
            previous_rating.delete()
        if interaction_serializer.is_valid():
            interaction_serializer.save(article = article, user = user)
            return Response(interaction_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(interaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['post'], detail=True, url_path="share")
    def share_article(self, request : Request, pk):
        user = request.user
        article = get_object_or_404(Article, pk = pk)
        data = {'article' : article.pk , 'user' : user.pk, **request.data}
        interaction_serializer = self.get_serializer_class()(data=data)
        if interaction_serializer.is_valid():
            interaction_serializer.save(article = article, user = user)
            return Response(interaction_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(interaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['post'], detail=True, url_path="favorite")
    def favorite_article(self, request : Request, pk):
        user = request.user
        article = get_object_or_404(Article, pk = pk)
        data = {'article' : article.pk , 'user' : user.pk, **request.data}
        interaction_serializer = self.get_serializer_class()(data=data)
        previous_rating = self.get_queryset().filter(user = user.pk , article = article.pk , interaction_type = "favorite")
        if len(previous_rating) > 0:
            previous_rating.delete()
            return Response("Removed From Favorite", status=status.HTTP_204_NO_CONTENT)
        elif interaction_serializer.is_valid():
            interaction_serializer.save(article = article, user = user)
            return Response(interaction_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(interaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewspaperViewset(viewsets.ModelViewSet):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer
    http_method_names = ['get', 'post', 'head', 'options', 'patch', 'delete']
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        if self.action == "create_article":
            return ArticleSerializer
        return self.serializer_class

    @action(methods=['post'], detail=True, url_path="create-article")
    def create_article(self, request, pk):
        newspaper = get_object_or_404(Newspaper, pk = pk)
        article_serializer = self.get_serializer_class()(data=request.data)
        if article_serializer.is_valid():
            article_serializer.save(newspaper=newspaper)
            return Response(article_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
