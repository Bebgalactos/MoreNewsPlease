from django.contrib.auth.models import BaseUserManager
from django.db import models
from uuid import uuid4
from .utils import generate_random_password


class UserManagerCustomised(BaseUserManager):

    def create_user(self, email, user_name, first_name, last_name, phone_number, adress, **extra_fields):
        if not email:
            raise ValueError("Adresse mail obligatoire")
        if not user_name:
            raise ValueError("Nom d'utilisateur obligatoire")
        if not first_name:
            raise ValueError("Prénom obligatoire")
        # if not last_name:
        #     raise ValueError("Nom obligatoire")
        # if not phone_number:
        #     raise ValueError("Num Tel obligatoire")
        # if not adress:
        #     raise ValueError("Adresse obligatoire")
        email = self.normalize_email(email)
        temporary_password = generate_random_password()
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name, phone_number=phone_number, adress=adress, temporary_password=temporary_password, ** extra_fields)
        user.set_password(temporary_password)
        user.save()
        return user

     # create super user
    def create_superuser(self, email, user_name, first_name, last_name, phone_number, adress, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, phone_number, adress, **extra_fields)
