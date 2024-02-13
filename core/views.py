from django.shortcuts import render, get_object_or_404
from store.models import Category, Product
from django.views.generic import TemplateView
from .models import Contact
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


# home page
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

# contact us
def contact(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['body']
        Contact.objects.create(first_name=first_name, last_name=last_name, email=email, body=body, subject=subject)
        messages.success(request, _('Your message succefully added'))

        return render(request, 'contact.html', context={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'subject': subject,
            'body': body
        })
    
        
    return render(request, 'contact.html')

# search product
def search(request):
    q = request.GET.get('q')
    products = Product.objects.filter(title__icontains=q)
    return render(request, 'product_list.html', context={'products': products})