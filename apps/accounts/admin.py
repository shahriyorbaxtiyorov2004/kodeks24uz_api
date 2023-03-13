from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

from .models import Account

admin.site.site_header = 'Kodeks24 Administration'
admin.site.unregister(BlacklistedToken)
admin.site.unregister(OutstandingToken)


@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
