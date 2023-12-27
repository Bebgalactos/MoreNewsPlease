
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, EmailConfirmationSerializer, UserSerialize
from django.core.mail import send_mail
from .models import EmailConfirmationModel
from rest_framework.permissions import IsAuthenticated
from uuid import uuid4


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            if not user.is_email_confirmed:
                return Response("Veuillez Activer Votre Compte. Vérifier votre adresse Mail", status=401)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)}, status=200)

        return Response("Email ou mot de passe incorrecte", status=403)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            CreateNewEmail(user_id=user.pk,
                           user_email=user.email, name=user.user_name)
            return Response("Compte crée avec succès. Veuillez Activer votre compte", status=201)
        else:
            return Response(serializer.errors, status=400)


class ConfirmEmail(APIView):
    def get(self, request):
        user_token = request.GET.get("token")
        email_id = request.GET.get("id")
        try:
            email = EmailConfirmationModel.objects.get(pk=email_id)
            user_id = RefreshToken(user_token).get("user_id")
        except:
            return Response("Lien d'activation invalide.", status=400)
        if (email.user.pk == user_id):
            if (email.user.is_email_confirmed):
                return Response("Compte déjà actif", 400)
            if (email.is_expired()):
                email.delete()
                CreateNewEmail(
                    user_id=user_id, user_email=email.user.email, name=email.user.user_name)
                return Response("Cet e-mail a expiré. Vous allez Recevoir un nouveau lien d'activation", status=406)
            email.user.is_email_confirmed = True
            email.user.save()
            email.delete()
            return Response("Compte activé avec succès")
        return Response("Lien d'activation invalide.", status=400)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # The user is already available if the request is authenticated
        serialized_user = UserSerialize(user).data
        return Response(serialized_user, status=200)


def CreateNewEmail(user_id, user_email, name):
    email_serializer = EmailConfirmationSerializer(data={
        "user": user_id,
    })
    if email_serializer.is_valid(raise_exception=True):
        email_serializer.save()
        # Send Confirmation mail
        send_mail(subject="Activation de compte MoreNewsPlease", message="Bonjour {name}, \n vous trouverez le lien d'activation de votre compte http://www.exemple.com".format(name=name),
                  from_email="rayene.zamouri@gmail.com", recipient_list=[user_email])
