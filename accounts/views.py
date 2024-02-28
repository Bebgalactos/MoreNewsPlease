from requests import get
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView , TokenBlacklistView
from rest_framework.response import Response
from MoreNewsPlease import settings
from drf_spectacular.utils import extend_schema
from accounts.serializers import TokenSerializer


class CustomTokenObtainView(TokenObtainPairView):
    @extend_schema(responses=TokenSerializer)
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Get the refresh token from the response
        if response.data is not None:
            refresh_token = response.data.get("refresh")
            # Set the refresh token as an HTTP-only cookie
            response.set_cookie(
                "refresh_token",
                refresh_token,
                httponly=True,
                max_age=settings.SIMPLE_JWT["SLIDING_TOKEN_REFRESH_LIFETIME"],
            )
            access_token = response.data.get("access")
            result = {"access": access_token}
            response.data = result
        return response


class CustomRefreshToken(TokenRefreshView):
    @extend_schema(request=None)
    def post(self, request, *args, **kwargs):
        request.data["refresh"] = request.COOKIES.get("refresh_token")  # type: ignore
        response = super().post(request, *args, **kwargs)
        return response

class CustomDestroyToken(TokenBlacklistView):
    @extend_schema(request=None)
    def post(self, request, *args, **kwargs):
        request.data["refresh"] = request.COOKIES.get("refresh_token")  # type: ignore
        response = super().post(request, *args, **kwargs)
        #delete the refresh token cookie
        response.delete_cookie("refresh_token")
        return response