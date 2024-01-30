from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'phone_Number', 'email', 'zip_code', 'city', 'address', 'order_notes', )
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'order_notes': forms.Textarea(attrs={'rows': 5, 'placeholder': 'If you have any notes write here, otherwise please it empty!'}),
            
        }