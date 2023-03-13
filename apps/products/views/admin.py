from rest_framework import generics, permissions

from apps.products.serializers import category
from apps.products.serializers import product


class CategoryCreateView(generics.CreateAPIView):
    queryset = category.Category.objects.all()
    serializer_class = category.CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.Category.objects.all()
    serializer_class = category.CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class BookCreateView(generics.CreateAPIView):
    queryset = product.Book.objects.all()
    serializer_class = product.BookSerializer
    permission_classes = [permissions.IsAdminUser]


class BookAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.Book.objects.all()
    serializer_class = product.Book
    permission_classes = [permissions.IsAdminUser]


class BookFormatCreateView(generics.CreateAPIView):
    queryset = product.BookFormat.objects.all()
    serializer_class = product.BookFormatSerializer
    permission_classes = [permissions.IsAdminUser]


class BookFormatAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.BookFormat.objects.all()
    serializer_class = product.BookFormatSerializer
    permission_classes = [permissions.IsAdminUser]


class BookImageCreateView(generics.CreateAPIView):
    queryset = product.BookImage.objects.all()
    serializer_class = product.BookImageSerializer
    permission_classes = [permissions.IsAdminUser]


class BookImageAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.BookImage.objects.all()
    serializer_class = product.BookImageSerializer
    permission_classes = [permissions.IsAdminUser]
