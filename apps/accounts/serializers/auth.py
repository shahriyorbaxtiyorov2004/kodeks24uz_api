from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt import serializers

Account = get_user_model()


class AccountLoginSerializers(serializers.TokenObtainPairSerializer):
    pass


class AccountLoginRefreshSerializers(serializers.TokenRefreshSerializer):
    pass


class AccountLogoutSerializers(serializers.TokenBlacklistSerializer):
    pass


class AccountRegisterSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'phone', 'first_name', 'last_name', 'password')
        read_only_fields = ('id', 'access_token', 'refresh_token')

    def create(self, validated_data):
        password = validated_data.pop('password')
        account = Account(**validated_data)
        account.set_password(password)
        account.save()
        return account
