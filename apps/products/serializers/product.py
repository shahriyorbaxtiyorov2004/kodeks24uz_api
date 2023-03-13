from rest_framework import serializers

from apps.products.models.product import Book, BookFormat, BookImage


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFormat
        fields = '__all__'


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = '__all__'
