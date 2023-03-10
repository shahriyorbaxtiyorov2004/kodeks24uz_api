from rest_framework import serializers

from apps.products.models import Book, Category, BookFormat


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookFormatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookFormat
        fields = '__all__'
