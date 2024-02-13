from .models import Category
from django.shortcuts import get_object_or_404
from cart.cart import Cart
from core.models import Information


def cart(request):
    return {'cart': Cart(request)}


def show_category(request, parent_id=None):

    category = Category.objects.prefetch_related('subs__subs').select_related('parent__parent')

    return { 'category': category}


def show_information(request):
    information = Information.objects.all().last()
    return {'information': information}