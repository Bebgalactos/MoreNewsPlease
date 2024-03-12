from os import read
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Category, Newspaper, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = ["newspaper_id", "name", "avatar_url"]


class ArticleSerializer(serializers.ModelSerializer):
    newspaper = NewspaperSerializer(read_only=True)
    categories = CategorySerializer(read_only=True, many=True)
    categories_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="categories", write_only=True, many=True
    )

    class Meta:
        model = Article
        fields = [
            "article_id",
            "title",
            "descritpion",
            "publication_date",
            "image_url",
            "author",
            "content",
            "newspaper",
            "article_interactions",
            "categories",
            "categories_ids",
        ]
        depth = 1


class UpdateArticleSerializer(ArticleSerializer):
    newspaper_id = serializers.PrimaryKeyRelatedField(
        queryset=Newspaper.objects.all(), source="newspaper", write_only=True
    )

    class Meta:
        model = Article
        fields = [
            "article_id",
            "title",
            "descritpion",
            "publication_date",
            "image_url",
            "author",
            "content",
            "newspaper",
            "article_interactions",
            "newspaper_id",
            "categories_ids",
            "categories",
        ]
        depth = 1
