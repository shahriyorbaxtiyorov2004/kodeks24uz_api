from django.contrib.auth import get_user_model
from rest_framework import serializers

Account = get_user_model()


class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'phone', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        account = super().update(instance, validated_data)
        if password:
            account.set_password(password)
            account.save()
        return account
