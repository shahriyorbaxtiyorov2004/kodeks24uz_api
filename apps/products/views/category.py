from rest_framework import generics, permissions

from apps.products.serializers import category


class CategoryListView(generics.ListAPIView):
    queryset = category.Category.objects.all()
    serializer_class = category.CategorySerializer
    permission_classes = [permissions.AllowAny]
