from store.models import Product
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from coupons.forms import CouponApplyForm
from coupons.models import Coupon
from decimal import Decimal




class Cart:
    def __init__(self, request):
        """
        Initialize the cart
        """


        self.request = request
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')
    
    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        Add the specified product to the cart if it exists
        """

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:

            self.cart[product_id]['quantity'] += quantity

        messages.success(self.request, _('Your product successfully add'))

        self.save()

    def remove(self, product):
        """
        Remove a product from the cart

        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]

        messages.success(self.request, _('Your product successfully removed'))

        self.save()

    def save(self):
        """
        Mark session as modified to save changes

        """
        self.session.modified = True

    def __iter__(self):

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:

            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            if item['product_obj'].discount:
                item['total_price'] = item['quantity'] * item['product_obj'].discount
            else:
                item['total_price'] = item['quantity'] * item['product_obj'].price

            yield item

    def __len__(self):
        
        return sum(item['quantity'] for item in self.cart.values())
        
    def clear(self):
        product_ids = self.cart.keys()

        del self.session['cart']

        self.save()

    def get_total_price(self):

        return sum((item['total_price'] for item in self.cart.values()))
    


    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None
    
    def get_discount(self):
        if self.coupon:
            return round((self.coupon.discount / Decimal('100')) * self.get_total_price(), 0)
        
    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
       
    
        

            

            
        

        
        

            
    




        





