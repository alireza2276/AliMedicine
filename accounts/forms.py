from django import forms

from allauth.account.forms import SignupForm, LoginForm
from django.utils.translation import gettext_lazy as _



class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label=_('first name'))
    last_name = forms.CharField(max_length=30, label=_('last name'))
    phone_number = forms.IntegerField(label=_('phone number'), required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']

        user.save()
        return user
    




