from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(_('title'), max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs', null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = _('Categories')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name=_('category'))
    title = models.CharField(_('title'), max_length=255)
    price = models.PositiveBigIntegerField(_('price'))
    discount = models.PositiveBigIntegerField(_('discount'), null=True, blank=True)
    image = models.ImageField(upload_to='static/product-image', verbose_name=_('image'))
    inventory = models.IntegerField()
    expire = models.CharField(_('expire'), max_length=255, blank=True, null=True)
    description = HTMLField(_('description'))
    short_description = HTMLField(_('short_description'), null=True, blank=True)
    country_created = models.CharField(_('country_created'), max_length=255, null=True, blank=True)
    volume = models.CharField(_('volume'), max_length=255, blank=True, null=True)
    gender = models.CharField(_('gender'), max_length=255, null=True, blank=True)
    number = models.CharField(_('number'), max_length=255, null=True, blank=True)
    length = models.CharField(_('length'), max_length=255, null=True, blank=True)
    compounds = models.TextField(_('compounds'), null=True, blank=True)
    special = models.CharField(_('special'), max_length=255, null=True, blank=True)
    

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modeified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])
    


    def __str__(self) -> str:
        return f"{self.title}"