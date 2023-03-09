from django.apps import AppConfig


class ProductsConfig(AppConfig):
    app_label = 'products'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'
    verbose_name = 'Products App'
