from .models import Category
from django.shortcuts import get_object_or_404
from cart.cart import Cart


def cart(request):
    return {'cart': Cart(request)}


def show_category(request, parent_id=None):

    category = Category.objects.prefetch_related('subs__subs').select_related('parent__parent')

    return { 'category': category}

