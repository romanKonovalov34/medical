from django import forms
from django.core.exceptions import ValidationError



from .models import User



class SigninForm(forms.Form):
    login = forms.CharField(max_length=50, label="Логин")
    password = forms.CharField(max_length=50, label="Пароль", widget=forms.PasswordInput())

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})



class RegisterForm(forms.Form):
    login = forms.CharField(max_length=50, label="Логин")
    password = forms.CharField(max_length=50, label="Пароль", widget=forms.PasswordInput())
    rePassword = forms.CharField(max_length=50, label="Повторите пароль", widget=forms.PasswordInput())
    
    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    rePassword.widget.attrs.update({'class': 'form-control'})