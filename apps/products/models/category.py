from django.utils.translation import gettext_lazy as _

from apps.shared import models as shared


class Category(shared.SlugModel, shared.BaseModel):
    class Meta:
        app_label = 'products'
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return str(self.name)
