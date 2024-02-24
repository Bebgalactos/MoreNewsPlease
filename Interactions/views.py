from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from Articles.models import Article
from .models import Interaction
from .serializers import (
    ReadSerializer, OpinionSerializer, ShareInteractionSerializer,
    RatingInteractionSerializer, FavoriteInteractionSerializer
)


class InteractionsViewset(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    # Mapping actions to serializers for easier access
    action_to_serializer = {
        "read_article": ReadSerializer,
        "opinion_article": OpinionSerializer,
        "share_article": ShareInteractionSerializer,
        "rate_article": RatingInteractionSerializer,
        "favorite_article": FavoriteInteractionSerializer,
    }

    def get_queryset(self):
        # Optimize queryset to fetch related articles in one query
        return Interaction.objects.select_related('article').filter(user=self.request.user)

    def get_serializer_class(self):
        return self.action_to_serializer.get(self.action)

    def perform_interaction(self, request, article_pk, interaction_type):
        """
        General method to perform an interaction, reducing repetitive code.
        """
        article = get_object_or_404(Article, pk=article_pk)
        serializer_class = self.get_serializer_class()
        data = {'article': article.pk, 'user': request.user.pk, **request.data}

        # Handle deletion for favorite and opinion updates
        if interaction_type in ['favorite', 'opinion', 'rating']:
            previous_interactions = Interaction.objects.filter(
                user__pk=request.user.pk, article__pk=article.pk, interaction_type=interaction_type).delete()
            if interaction_type == 'favorite' and previous_interactions[0] > 0:
                return Response("removed from favorite", status=status.HTTP_204_NO_CONTENT)

        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, url_path="read_article")
    def read_article(self, request, article_pk):
        return self.perform_interaction(request, article_pk, 'read')

    @action(methods=['post'], detail=False, url_path="opinion")
    def opinion_article(self, request, article_pk):
        return self.perform_interaction(request, article_pk, 'opinion')

    @action(methods=['post'], detail=False, url_path="rate")
    def rate_article(self, request, article_pk):
        return self.perform_interaction(request, article_pk, 'rating')

    @action(methods=['post'], detail=False, url_path="share")
    def share_article(self, request, article_pk):
        return self.perform_interaction(request, article_pk, 'share')

    @action(methods=['post'], detail=False, url_path="favorite")
    def favorite_article(self, request, article_pk):
        return self.perform_interaction(request, article_pk, 'favorite')
