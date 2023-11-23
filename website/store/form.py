import logging

from django import forms
from .models import Customer


class UserForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=100)
    email_address = forms.EmailField()
    phone_number = forms.CharField(min_length=9, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)

    def clean_email_address(self):
        Email = self.cleaned_data.get('email_address')
        if Customer.objects.filter(email_address=Email).exists():
            raise forms.ValidationError('that email already exist')
        else:
            return Email


    def save(self, *args, **kwargs):
        nm = self.cleaned_data.get('username')
        em = self.cleaned_data.get('email_address')
        tl = self.cleaned_data.get('phone_number')
        pw = self.cleaned_data.get('password')

        return Customer.objects.create_user(username=nm, email_address=em, phone_number=tl, password=pw)
