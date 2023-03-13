from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared import models as shared


class Book(shared.SlugModel, shared.BaseModel):
    class Language(models.TextChoices):
        UZB_RUS = ('uzb/rus', 'o\'zb/rus',)
        UZB = ('uzbek', 'o\'zbek',)
        RUS = ('russian', 'ruscha',)
        CYR = ('cyrillic', 'krill',)
        ENG = ('english', 'ingliz',)

    class Cover(models.TextChoices):
        HARD = ('hard', 'buvimli',)
        SOFT = ('soft', 'yumshoq',)

    image = models.OneToOneField('BookImage', on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    inStock = models.PositiveIntegerField(default=1 if available else 0)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    full_title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000, null=True)

    language = models.CharField(max_length=15, choices=Language.choices, default=Language.UZB)
    volume = models.PositiveIntegerField(default=1)
    format = models.ForeignKey('BookFormat', on_delete=models.SET_NULL, null=True)
    ISBN = models.CharField(max_length=25, unique=True)
    cover = models.CharField(max_length=15, choices=Cover.choices, default=Cover.HARD)

    info = models.JSONField(null=True, blank=True)

    class Meta:
        app_label = 'products'
        ordering = ('full_title',)
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):
        return self.name


class BookFormat(models.Model):
    height = models.PositiveIntegerField(default=50)
    width = models.PositiveIntegerField(default=50)
    type = models.PositiveIntegerField(default=1)

    class Meta:
        app_label = 'products'
        verbose_name = _("book format")
        verbose_name_plural = _("book formats")

    def __str__(self):
        return self.format()

    def format(self):
        return f'{self.height}x{self.width}/{self.type}'


class BookImage(shared.SlugModel, shared.BaseModel):
    image = models.ImageField(max_length=150, upload_to=f'products/images/')

    class Meta:
        app_label = 'products'
        verbose_name = _("book image")
        verbose_name_plural = _("book images")

    def __str__(self):
        return self.image.url
