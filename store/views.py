from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product



class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

