from rest_framework import serializers
from .models import Channel, Article

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('channel_id', 'name', 'avatar_url')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('article_id', 'title', 'descritpion', 'publication_date', 'image_url', 'channel')

class ArticleReadSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only = True)
    class Meta: 
        model = Article
        fields = ('article_id', 'title', 'descritpion', 'publication_date', 'image_url', 'channel')