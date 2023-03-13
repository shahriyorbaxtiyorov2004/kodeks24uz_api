from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework_simplejwt import views

from apps.accounts.serializers import auth

Account = get_user_model()


class AccountLoginView(views.TokenObtainPairView):
    serializer_class = auth.AccountLoginSerializers
    permission_classes = [permissions.AllowAny]


class AccountLoginRefreshView(views.TokenRefreshView):
    serializer_class = auth.AccountLoginRefreshSerializers


class AccountLogoutView(views.TokenBlacklistView):
    serializer_class = auth.AccountLogoutSerializers
    permission_classes = [permissions.IsAuthenticated]


class AccountRegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = auth.AccountRegisterSerializer
    permission_classes = [permissions.AllowAny]
