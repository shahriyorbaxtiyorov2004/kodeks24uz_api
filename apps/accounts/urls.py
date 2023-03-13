from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.accounts.views import accounts, auth, admin

router = DefaultRouter()
router.register('', admin.AccountAdminViewSet)

urlpatterns = [
    path('profile-login/', auth.AccountLoginView.as_view(), name='login'),
    path('profile-login/refresh/', auth.AccountLoginRefreshView.as_view(), name='login-refresh'),
    path('profile-register/', auth.AccountRegisterView.as_view(), name='register'),
    path('profile-logout/', auth.AccountLogoutView.as_view(), name='logout'),

    path('profile/', accounts.AccountView.as_view(), name='profile-detail'),

    path('admin-view-profiles/', include(router.urls), name='admin-view-profiles'),
]
