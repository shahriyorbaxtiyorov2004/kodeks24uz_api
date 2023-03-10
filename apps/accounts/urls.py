from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from apps.accounts import views
from apps.accounts.views import AccountAdminViewSet

router = DefaultRouter()
router.register('', AccountAdminViewSet)

urlpatterns = [
    path('profile-login/', TokenObtainPairView.as_view(), name='login'),
    path('profile-login/refresh/', TokenRefreshView.as_view(), name='login-refresh'),
    path('profile-register/', views.AccountRegisterView.as_view(), name='register'),
    path('profile-logout/', TokenBlacklistView.as_view(), name='logout'),

    path('my-profile/', views.AccountView.as_view(), name='profile-detail'),

    path('profiles/', include(router.urls), name='profiles'),
]
