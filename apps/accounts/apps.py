from django.apps import AppConfig


class AccountsConfig(AppConfig):
    app_label = 'accounts'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    verbose_name = 'Accounts App'
