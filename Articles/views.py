from rest_framework import viewsets, status, mixins
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Article, Category, Newspaper
from Interactions.models import Interaction
from .serializers import (
    ArticleSerializer,
    CategorySerializer,
    NewspaperSerializer,
    UpdateArticleSerializer,
)
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from django_filters import rest_framework as filters
from .filters import ArticleFilters


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ["get", "head", "options", "put", "delete"]
    permission_classes = [IsAuthenticated]
    filter_backends = (
        filters.DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_class = ArticleFilters

    def get_queryset(self):
        user = self.request.user
        return self.queryset.prefetch_related(
            Prefetch(
                "article_interactions", queryset=Interaction.objects.filter(user=user)
            )
        )

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return UpdateArticleSerializer
        return self.serializer_class


class NewspaperViewset(viewsets.ModelViewSet):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer
    http_method_names = ["get", "post", "head", "options", "put", "delete"]
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name"]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in [
            "create",
            "update",
            "partial_update",
            "destroy",
            "create_article",
        ]:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "create_article":
            return ArticleSerializer
        return self.serializer_class

    @action(methods=["post"], detail=True, url_path="create-article")
    def create_article(self, request, pk):
        newspaper = get_object_or_404(Newspaper, pk=pk)
        categories = request.data.pop("categories", [])
        categories_ids = [category["id"] for category in categories]
        article_serializer = self.get_serializer_class()(data=request.data)
        if article_serializer.is_valid():
            article_serializer.save(newspaper=newspaper, categories=categories_ids)
            return Response(article_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                article_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class CategoryViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()
