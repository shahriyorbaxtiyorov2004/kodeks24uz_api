from django.urls import path, include

urlpatterns = [
    path('accounts/', include('apps.accounts.urls')),
    path('products/', include('apps.products.urls')),
    path('orders/', include('apps.orders.urls')),

]
