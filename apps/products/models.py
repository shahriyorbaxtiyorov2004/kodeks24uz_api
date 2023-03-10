from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared import models as shared


# Create your models here.
class Category(shared.SlugModel, shared.BaseModel):
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return str(self.name)


class BookFormat(models.Model):


    type = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = _("book_format")
        verbose_name_plural = _("book_formats")

    def __str__(self):
        return str(self.type)


class Book(shared.SlugModel, shared.BaseModel):
    class Language(models.TextChoices):
        UZB_RUS = 'uzb/rus'
        UZB = 'uzb'
        RUS = 'rus'
        CYR = 'cyr'
        ENG = 'eng'

    class Cover(models.TextChoices):
        HARD = 'hard'
        SOFT = 'soft'

    image = models.ImageField(max_length=150, upload_to=f'products/images/')

    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    full_title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)

    language = models.CharField(max_length=15, choices=Language.choices, default=Language.UZB)
    volume = models.PositiveIntegerField(default=1)
    format = models.ForeignKey('BookFormat', on_delete=models.SET_NULL, null=True)
    ISBN = models.CharField(max_length=13, unique=True)
    cover = models.CharField(max_length=15, choices=Cover.choices, default=Cover.HARD)

    info = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ('full_title',)
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):
        return self.name
