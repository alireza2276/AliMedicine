from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from .cart import Cart
from .forms import AddToCartForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from coupons.forms import CouponApplyForm



def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddToCartForm(initial={
            'quantity' : item['quantity'], 
            'inplace': True,
        })

    coupon_apply_form = CouponApplyForm()

    return render(request, 'cart_detail.html', context={
        'cart': cart,
        'coupon_apply_form': coupon_apply_form
    })

def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product.objects.select_related('category').all(), id=product_id)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']

        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    cart.remove(product)

    return redirect('cart_detail')

def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _('Your cart successfully removed from your cart'))

    else:
        messages.warning(request, _('Your cart is empty'))

    return redirect('product_list')


