from django.db import models
from django.utils.translation import gettext_lazy as _



class Contact(models.Model):
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    email = models.EmailField(_('email'))
    subject = models.CharField(_('subject'), max_length=255)
    body = models.TextField(_('body'))

    class Meta:
        verbose_name_plural = _('contacts')


    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name}"


class Information(models.Model):
    address = models.CharField(_('address'), max_length=255)
    phone_number = models.IntegerField(_('phone_number'))
    email = models.EmailField(_('email'))

    class Meta:
        verbose_name_plural = _('informations')

    def __str__(self) -> str:
        return self.address