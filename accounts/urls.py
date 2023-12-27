from django.urls import path
from .views import RegisterView, LoginView, ConfirmEmail, ProfileView
urlpatterns = [
    path('register', view=RegisterView.as_view()),
    path('login', view=LoginView.as_view()),
    path('verify-email/', view=ConfirmEmail.as_view()),
    path('profile/', view=ProfileView.as_view())
]
