from django.contrib import admin
from .models import Contact, Information


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'subject']


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ['email', 'address', 'phone_number', ]
