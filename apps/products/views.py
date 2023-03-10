from rest_framework import generics, permissions, viewsets

from apps.products.models import Book, Category
from apps.products.serializers import BookSerializer, CategorySerializer, BookFormatSerializer


# Categories
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]


# Books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAdminUser]


# BookParts
class BookFormatViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookFormatSerializer
    permission_classes = [permissions.IsAdminUser]
