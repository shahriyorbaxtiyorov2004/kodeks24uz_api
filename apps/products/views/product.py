from rest_framework import generics, permissions

from apps.products.serializers import product


class BookListView(generics.ListAPIView):
    queryset = product.Book.objects.all()
    serializer_class = product.BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    queryset = product.Book.objects.all()
    serializer_class = product.BookSerializer
    permission_classes = [permissions.AllowAny]
