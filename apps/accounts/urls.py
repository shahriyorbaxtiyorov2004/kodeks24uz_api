from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from apps.accounts import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('profile/', views.AccountView.as_view(), name='profile'),
]
