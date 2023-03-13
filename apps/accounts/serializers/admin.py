from django.contrib.auth import get_user_model
from rest_framework import serializers

Account = get_user_model()


class AccountAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
