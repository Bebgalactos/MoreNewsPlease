from rest_framework import serializers
from .models import Newspaper, Article

class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = ['newspaper_id', 'name', 'avatar_url']

class ArticleSerializer(serializers.ModelSerializer):
    newspaper = NewspaperSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['article_id', 'title', 'descritpion', 'publication_date', 'image_url', 'author', 'content', 'newspaper','article_interactions']
        depth = 1