from django.db import models
from django.conf import settings
from store.models import Product
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Order(models.Model):
        customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name=_('customer') )
        is_paid = models.BooleanField(_('is_paid'), default=False)

        first_name = models.CharField(_('first_name'), max_length=255)
        last_name = models.CharField(_('last_name'), max_length=255)

        phone_Number = models.CharField(_('phone_number'), max_length=15)
        address = models.CharField(_('address'), max_length=700)
        order_notes = models.CharField(_('order_notes'), max_length=700, blank=True)

        city = models.CharField( _('city'), max_length=255)
        zip_code = models.CharField(_('zipcode'), max_length=255)
        email = models.EmailField(_('email'))


        datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True)
        datetime_modified = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f"{self.customer} - {self.is_paid}"
        
        class Meta:
            verbose_name_plural = _('orders')

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('order'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item', verbose_name=_('product'))
    quantity = models.PositiveIntegerField(_('quantity'),default=1)
    price = models.PositiveIntegerField(_('price'),)

    def __str__(self):
        return f"OrderItems {self.id} : {self.product} x {self.quantity}  (price:{self.price})"
    
    class Meta:
        verbose_name_plural = _('orderitems')