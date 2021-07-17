from django import forms
from register.models import Register


class Registration_form(forms.Form):
    user_name = forms.CharField(
        max_length=100)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(
        max_length=200,  widget=forms.PasswordInput)


class login_form(forms.Form):
    user_name = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
