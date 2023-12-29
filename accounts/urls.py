from django.urls import path
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView


app_name = 'accounts'

urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'create'}), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
    path("activation/", UserViewSet.as_view({"post": "activation"}), name="activate"),
    path("reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path("reset-password-confirm/", UserViewSet.as_view({"post": "reset_password_confirm"}), name="reset_password_confirm"),
    path("change-email/", UserViewSet.as_view({"post": "reset_username"}), name="change_email"),
    path("change-email-confirm/", UserViewSet.as_view({"post": "reset_username_confirm"}), name="change_email_confirm")
]
