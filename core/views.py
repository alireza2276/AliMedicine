from django.shortcuts import render, get_object_or_404
from store.models import Category, Product
from django.views.generic import TemplateView


def home(request):
    products = Product.objects.order_by('datetime_created')[:6]
    percentages = Product.objects.all()
    return render(request, 'home.html', context={
        'products': products,
        'percentages': percentages
    })

def category(request, pk=None):
    categories = get_object_or_404(Category, id=pk)
    products = categories.products.all()
    return render(request, 'product_list.html', context={
        'categories': categories,
        'products': products
    })
