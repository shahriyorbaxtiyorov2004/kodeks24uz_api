from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from apps.accounts.serializers import admin

Account = get_user_model()


class AccountAdminViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = admin.AccountAdminSerializer
    permission_classes = [permissions.IsAdminUser]
