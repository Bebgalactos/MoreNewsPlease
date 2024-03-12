from rest_framework import serializers
from .models import UserCustomised
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from djoser.serializers import ActivationSerializer
from djoser.utils import decode_uid
from .utils import generate_random_password
# Serializer to Register User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserCustomised.objects.all())]
    )
    phone_number = serializers.CharField(required=True, validators=[RegexValidator(
        regex="^(?:(?:(?:\+|00)33[ ]?(?:\(0\)[ ]?)?)|0){1}[1-9]{1}([ .-]?)(?:\d{2}\1?){3}\d{2}$",
        message="Format Tel Invalide"),
        UniqueValidator(queryset=UserCustomised.objects.all())])
    is_first_login = serializers.BooleanField(read_only=True)

    class Meta:
        model = UserCustomised
        fields = ('id','user_name', 'email', 'first_name', 'last_name',
                  'phone_number', 'adress', "is_first_login")
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
            'adress': {'required': True}}

    def create(self, validated_data):
        temporary_password = generate_random_password()
        user = UserCustomised.objects.create(
            user_name=validated_data['user_name'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            adress=validated_data['adress'],
            temporary_password=temporary_password
        )
        user.set_password(temporary_password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomised
        fields = ['id', 'user_name', 'first_name',
                  'last_name', 'email', 'phone_number', 'adress', 'is_first_login', 'is_active' , 'is_staff', 'algorithm']
        
    def delete(self, validated_data):
        user = UserCustomised.objects.get(id=validated_data['id'])
        user.delete()
        return user


class AccountActivationSerializer(ActivationSerializer):
    old_password = serializers.CharField(
        write_only=True, required=True)
    new_password = serializers.CharField(
        write_only=True, required=True)

    def validate(self, data):
        attrs = super().validate(data)
        old_password = data["old_password"]
        new_password = data["new_password"]
        user_object = self.user
        if not user_object.is_first_login:
            raise serializers.ValidationError("Compte déjà activé")

        if not user_object.check_password(old_password):
            raise serializers.ValidationError("Ancien mot de passe erroné")

        user_object.set_password(new_password)
        user_object.is_first_login = False
        user_object.temporary_password = ""
        user_object.save()
        return attrs

class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()

    def validate(self, attrs):
        return attrs