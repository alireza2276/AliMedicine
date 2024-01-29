from django.contrib import admin
from .models import Category, Product
from django.contrib.admin import ModelAdmin
from django.db.models import Count
from django.http.request import HttpRequest
from django.db.models.query import QuerySet
from typing import Any




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory', 'datetime_created']


