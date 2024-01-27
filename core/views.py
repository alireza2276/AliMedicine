from django.shortcuts import render, get_object_or_404
from store.models import Category
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home.html')

def category(request, pk=None):
    categories = get_object_or_404(Category, id=pk)
    products = categories.products.all()
    return render(request, 'product_list.html', context={
        'categories': categories,
        'products': products
    })
