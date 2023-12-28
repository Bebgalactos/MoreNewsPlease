from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer, ChannelSerializer, ArticleReadSerializer
from .models import Article, Channel
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class ArticleView(APIView):
    serializer_class = ArticleReadSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id is None:
            articles = Article.objects.all()
            serialize = self.serializer_class(articles, many=True)
            return Response(serialize.data, status=200)
        else:
            try:
                article = Article.objects.get(pk=id)
            except:
                return Response("Article n'existe pas", status=404)
            serialize = self.serializer_class(article)
            return Response(serialize.data, status=200)

    def post(self, request):

        try:
            channel = Channel.objects.get(pk=request.data["channel"])
        except:
            return Response("Channel not foud", status=400)
        serializer = ArticleSerializer(
            data={**request.data, channel: channel.pk})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Article Successfully Created!", status=201)
        return Response(serializer.errors, status=404)

    def patch(self, request, id):
        try:
            article = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return Response("Article n'existe pas", status=404)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        try:
            article = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return Response("Article n'existe pas", status=404)
        article.delete()
        return Response("Article supprimé", status=204)


class ChannelView(APIView):
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id is None:
            channels = Channel.objects.all()
            serialize = self.serializer_class(channels, many=True)
            return Response(serialize.data, status=200)
        else:
            try:
                channel = Channel.objects.get(pk=id)
            except:
                return Response("Channel n'existe pas", status=404)
            serialize = self.serializer_class(channel)
            return Response(serialize.data, status=200)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, id):
        try:
            channel = Channel.objects.get(pk=id)
        except Channel.DoesNotExist:
            return Response("Le channel n'a pas été trouvé.", status=404)
        serializer = self.serializer_class(channel, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        try:
            channel = Channel.objects.get(pk=id)
        except Channel.DoesNotExist:
            return Response("Le channel n'a pas été trouvé.", status=404)
        channel.delete()
        return Response("Le channel a bien été supprimé.", status=200)
