from requests import get
from rest_framework import viewsets
from rest_framework.decorators import action
from recommendations.models import Recommendation
from .serializers import RecommendationReadSerializer, RecommendationWriteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class RecommendationViewSet(
    viewsets.GenericViewSet,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.CreateModelMixin,
):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationReadSerializer
    permission_classes = ()

    def get_serializer_class(self):
        if self.action in ["create"]:
            return RecommendationWriteSerializer
        return RecommendationReadSerializer

    def get_permissions(self):
        if self.action in ["create", "list", "get_recommendations_by_user"]:
            return []
        return [IsAuthenticated]

    @action(
        detail=False,
        methods=["get"],
        url_path="list",
    )
    def list_recommendations(self, request):
        user = request.user
        recommendation = self.queryset.filter(user=user).order_by("-timestamp")[0]
        serializer = self.get_serializer(recommendation)
        articleList = serializer.data["articleList"]
        return Response(articleList, status=status.HTTP_200_OK)

    # get recommendations by user id
    @action(detail=False, methods=["get"], url_path="(?P<user_id>[^/.]+)")
    def get_recommendations_by_user(self, request, user_id):
        user = user_id
        recommendation = self.queryset.filter(user=user).order_by("-timestamp")
        serializer = self.get_serializer(recommendation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
