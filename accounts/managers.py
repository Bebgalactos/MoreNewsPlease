from django.contrib.auth.models import BaseUserManager
from django.db import models
from uuid import uuid4


class UserManagerCustomised(BaseUserManager):

    def create_user(self, email, password, user_name, first_name, last_name, phone_number, adress, **extra_fields):
        if not email:
            raise ValueError("Adresse mail obligatoire")
        if not user_name:
            raise ValueError("Nom d'utilisateur obligatoire")
        if not first_name:
            raise ValueError("Prénom obligatoire")
        if not last_name:
            raise ValueError("Nom obligatoire")
        if not phone_number:
            raise ValueError("Num Tel obligatoire")
        if not adress:
            raise ValueError("Adresse obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name, phone_number=phone_number, adress=adress, **extra_fields)
        user.set_password(password)
        user.save()
        return user

     # create super user
    def create_superuser(self, email, password, user_name, first_name, last_name, phone_number, adress, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_email_confirmed", True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, user_name, first_name, last_name, phone_number, adress, **extra_fields)


class EmailConfirmationManager(models.Manager):
    def create_email_confirmation(self, user):
        return self.create(user=user)
