from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models.product import Book, BookFormat, BookImage
from .models.category import Category


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ['image', 'name', 'price']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BookFormat)
class BookFormatAdmin(ImportExportModelAdmin):
    pass


@admin.register(BookImage)
class BookImageAdmin(ImportExportModelAdmin):
    list_display = ('image', 'name',)
    prepopulated_fields = {'slug': ('name',)}
