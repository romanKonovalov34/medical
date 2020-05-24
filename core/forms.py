from django import forms
from django.core.exceptions import ValidationError


from .models import User
#from .models import Doctor
from .models import Patient



class SigninForm(forms.Form):
    login = forms.CharField(max_length=50, label="Логин")
    password = forms.CharField(max_length=50, label="Пароль", widget=forms.PasswordInput())
    isAdmin = forms.BooleanField(required=False, label='Я администратор')

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    isAdmin.widget.attrs.update({'class': 'form-control'})



class RegisterForm(forms.Form):
    login = forms.CharField(max_length=50, label="Логин")
    password = forms.CharField(max_length=50, label="Пароль", widget=forms.PasswordInput())
    rePassword = forms.CharField(max_length=50, label="Повторите пароль", widget=forms.PasswordInput())
    
    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    rePassword.widget.attrs.update({'class': 'form-control'})

    

class DbPatientsForm(forms.Form):
    number_card = forms.CharField(required='', max_length=50, label="Номер карты")
    FIO = forms.CharField(required='', max_length=100, label="ФИО")
    date_birth = forms.CharField(required='', label='Дата рождения', widget=forms.TextInput(attrs={'placeholder': 'Пожалуйста, используйте следующий формат: ДД.ММ.ГГГГ'}))
    sex = forms.CharField(required='', max_length=50, label="Пол")
    nationality = forms.CharField(required='', max_length=50, label="Национальность")
    education = forms.CharField(required='', max_length=100, label="Образование")
    address = forms.CharField(required='', max_length=100, label="Адрес")
    phone = forms.CharField(required='', max_length=50, label="Телефон")
    job = forms.CharField(required='', max_length=100, label="Место работы")
    position = forms.CharField(required='', max_length=100, label="Должность")

    number_card.widget.attrs.update({'class': 'form-control'})
    FIO.widget.attrs.update({'class': 'form-control'})
    date_birth.widget.attrs.update({'class': 'form-control'})
    sex.widget.attrs.update({'class': 'form-control'})
    nationality.widget.attrs.update({'class': 'form-control'})
    education.widget.attrs.update({'class': 'form-control'})
    address.widget.attrs.update({'class': 'form-control'})
    phone.widget.attrs.update({'class': 'form-control'})
    job.widget.attrs.update({'class': 'form-control'})
    position.widget.attrs.update({'class': 'form-control'})

