from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from cart.cart import Cart
from.forms import OrderForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _




def order_create(request):
    cart = Cart(request)
    order_form = OrderForm()

    if not len(cart):
        messages.warning(request, _('You can not proceed, because your cart is empty!'))
        return redirect('product_list')
    
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

        
            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order = order_obj,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price,
                )
            
            cart.clear()

            messages.success(request, _('Your orders has successfully placed.'))


            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()
    
    return render(request, 'order_create.html', context={
        'form': order_form
    })


    

