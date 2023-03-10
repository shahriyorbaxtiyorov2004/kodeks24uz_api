from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt import views

from . import serializers
from .models import Account


class AccountAdminViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = serializers.AccountAdminSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class AccountLoginView(views.TokenObtainPairView):
    serializer_class = serializers.AccountLoginSerializers
    permission_classes = [permissions.AllowAny]


class AccountLoginRefreshView(views.TokenRefreshView):
    serializer_class = serializers.AccountLoginRefreshSerializers


class AccountLogoutView(views.TokenBlacklistView):
    serializer_class = serializers.AccountLogoutSerializers
    permission_classes = [permissions.IsAuthenticated]


class AccountRegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountModelSerializer
    permission_classes = [permissions.AllowAny]


class AccountView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
