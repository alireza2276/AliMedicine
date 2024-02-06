from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category



class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        request = self.request
        categories_obj = Category.objects.all().order_by('subs')
        categories = request.GET.getlist('categories')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        products = Product.objects.select_related('category').all()

        if len(categories):

            products = products.filter(category__title__in=categories).distinct()

        if min_price and max_price:
            products = products.filter(price__lte=max_price, price__gte=min_price)

        context['products'] = products
        context['catgeories'] = categories
        context['categories_obj'] = categories_obj
        return context




class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

