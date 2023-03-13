from django.urls import path

from apps.products.views import admin
from apps.products.views import category
from apps.products.views import product

urlpatterns = [
    path('books/all', product.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', product.BookDetailView.as_view(), name='book-detail'),

    path('categories/all', category.CategoryListView.as_view(), name='book-list'),

    # admin
    path('admin-books/create/', admin.BookCreateView.as_view(), name='book-create'),
    path('admin-books/<int:pk>/', admin.BookAdminView.as_view(), name='book-update'),
    path('admin-categories/create/', admin.CategoryCreateView.as_view(), name='book-create'),
    path('admin-categories/<int:pk>/', admin.CategoryAdminView.as_view(), name='book-update'),
]
