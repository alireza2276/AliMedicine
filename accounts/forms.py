from django import forms

from allauth.account.forms import SignupForm, LoginForm



class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Fist Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone_number = forms.IntegerField(label='Phone Number', required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']

        user.save()
        return user
    




