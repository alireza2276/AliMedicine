from django.contrib import admin
from django.contrib import admin
from .models import Order, OrderItem
from django.contrib.admin import ModelAdmin
from django.db.models import Count
from django.http.request import HttpRequest
from django.db.models.query import QuerySet
from typing import Any

# Register your models here.


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'quantity', 'product', 'price']
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','datetime_created', 'is_paid', 'num_of_items']
    inlines = [OrderItemTabularInline]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related('items').annotate(items_count=Count('items'))
    @admin.display(ordering='items_count')
    def num_of_items(self, order):
        return order.items_count


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']