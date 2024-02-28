from django.urls import path
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView , TokenBlacklistView , TokenRefreshView

from accounts.views import CustomDestroyToken, CustomRefreshToken, CustomTokenObtainView


app_name = 'accounts'

urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'create'}), name="register"),
    path("login/", CustomTokenObtainView.as_view(), name="login"),
    path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
    path("activation/", UserViewSet.as_view({"post": "activation"}), name="activate"),
    path("reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("reset-password-confirm/", UserViewSet.as_view({"post": "reset_password_confirm"}), name="reset_password_confirm"),
    path("change-email/", UserViewSet.as_view({"post": "set_username"}), name="change_email"),
    path("profile/", UserViewSet.as_view({"get": "me"}), name="profile"),
    path("edit-profile/", UserViewSet.as_view({"patch": "me"}), name="profile_edit"),
    path("delete-profile/", UserViewSet.as_view({"delete": "me"}), name="profile_delete"),
    path("logout/",CustomDestroyToken.as_view(), name='logout'),
    path("refresh/", CustomRefreshToken.as_view(), name="refresh_token")
]
