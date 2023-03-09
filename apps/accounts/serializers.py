from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt import serializers as jwt_s

from apps.accounts.models import Account


class AccountLoginSerializers(jwt_s.TokenObtainPairSerializer):
    pass


class AccountLoginRefreshSerializers(jwt_s.TokenRefreshSerializer):
    pass


class AccountLogoutSerializers(jwt_s.TokenBlacklistSerializer):
    pass


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'phone', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Account.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password')
        if password:
            validate_password(password)
            instance.set_password(password)
        instance.save()
        return instance
