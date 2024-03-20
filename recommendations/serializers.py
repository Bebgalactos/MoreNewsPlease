from rest_framework import serializers

from Articles.serializers import ArticleSerializer
from Articles.models import Article
from accounts.models import UserCustomised
from .models import Recommendation

class RecommendationReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = "__all__"

class RecommendationWriteSerializer(serializers.ModelSerializer):
    articleList = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(), many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=UserCustomised.objects.all(), many=True)
    class Meta:
        model = Recommendation
        fields = ("articleList", "user")