from django.urls import path
from .views import RegisterView, LoginView, ConfirmEmail, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('register', view=RegisterView.as_view(),name="Register"),
    path('login', view=LoginView.as_view(),name="Login"),
    path('verify-email/', view=ConfirmEmail.as_view(),name="verify email"),
    path('profile/', view=ProfileView.as_view(),name="get profile")
]
