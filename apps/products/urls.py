from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'book-format', views.BookFormatViewSet)

urlpatterns = [
    path('books/all', views.BookListView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),

    path('categories/all', views.CategoryListView.as_view(), name='book-list'),

    # path('categories/create/', views.CategoryCreateView.as_view(), name='book-create'),
    # path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='book-detail'),
    # path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='book-update'),
    # path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='book-delete'),

    # path('', include(router.urls)),
]
