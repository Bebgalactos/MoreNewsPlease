from rest_framework import serializers
from .models import UserCustomised
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password

# Serializer to Register User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserCustomised.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(required=True, validators=[RegexValidator(
        regex="^(?:(?:(?:\+|00)33[ ]?(?:\(0\)[ ]?)?)|0){1}[1-9]{1}([ .-]?)(?:\d{2}\1?){3}\d{2}$",
        message="Format Tel Invalide"),
        UniqueValidator(queryset=UserCustomised.objects.all())])

    class Meta:
        model = UserCustomised
        fields = ('user_name', 'password', 'password2',
                  'email', 'first_name', 'last_name', 'phone_number', 'adress')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
            'adress': {'required': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = UserCustomised.objects.create(
            user_name=validated_data['user_name'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            adress=validated_data['adress']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = UserCustomised
        fields = ['id', 'user_name', 'first_name',
                  'last_name', 'email', 'phone_number', 'adress']


