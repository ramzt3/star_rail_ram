from django import forms

from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'password'
    }))
