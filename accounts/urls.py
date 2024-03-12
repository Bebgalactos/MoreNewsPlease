from django.urls import path
from accounts.views import CustomDestroyToken, CustomRefreshToken, CustomTokenObtainView , CustomUserViewset


app_name = "accounts"

urlpatterns = [
    path("register/", CustomUserViewset.as_view({"post": "create"}), name="register"),
    path("login/", CustomTokenObtainView.as_view(), name="login"),
    path("users/", CustomUserViewset.as_view({"get": "list"}), name="users"),
    path("users/<int:id>/", CustomUserViewset.as_view({"get": "retrieve"}), name="user"),
    path(
        "users/<int:id>/update/",
        CustomUserViewset.as_view({"put": "update"}),
        name="user_update",
    ),
    path(
        "users/<int:id>/delete/",
        CustomUserViewset.as_view({"delete": "destroy"}),
        name="user_delete",
    ),
    path(
        "resend-activation/",
        CustomUserViewset.as_view({"post": "resend_activation"}),
        name="resend_activation",
    ),
    path("activation/", CustomUserViewset.as_view({"post": "activation"}), name="activate"),
    path(
        "reset-password/",
        CustomUserViewset.as_view({"post": "reset_password"}),
        name="reset_password",
    ),
    path(
        "reset-password-confirm/",
        CustomUserViewset.as_view({"post": "reset_password_confirm"}),
        name="reset_password_confirm",
    ),
    path(
        "change-email/",
        CustomUserViewset.as_view({"post": "set_username"}),
        name="change_email",
    ),
    path("profile/", CustomUserViewset.as_view({"get": "me"}), name="profile"),
    path("edit-profile/", CustomUserViewset.as_view({"put": "me"}), name="profile_edit"),
    path(
        "delete-profile/", CustomUserViewset.as_view({"delete": "me"}), name="profile_delete"
    ),
    path("logout/", CustomDestroyToken.as_view(), name="logout"),
    path("refresh/", CustomRefreshToken.as_view(), name="refresh_token"),
    path(
        "change-password/",
        CustomUserViewset.as_view({"post": "set_password"}),
        name="change_password",
    ),
    path(
        "change-email/",
        CustomUserViewset.as_view({"post": "set_username"}),
        name="change_email",
    ),
]
