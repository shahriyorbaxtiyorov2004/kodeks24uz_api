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


class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'phone', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        account = Account(**validated_data)
        account.set_password(password)
        account.save()
        return account

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        account = super().update(instance, validated_data)
        if password:
            account.set_password(password)
            account.save()
        return account
