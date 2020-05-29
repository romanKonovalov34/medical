from django import forms
from django.core.exceptions import ValidationError


from .models import User
#from .models import Doctor
from .models import Patient
from .models import Ancket



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

# анкета
class DBFormsForm(forms.Form):

    number_ancket = forms.CharField(required='', label="Номер анкеты")
    question = forms.CharField(required='', label="Вопрос")
    answer = forms.CharField(required='', label="Ответ")
    conviction = forms.CharField(required='', label="Уверенность")

    number_ancket.widget.attrs.update({'class': 'form-control'})
    question.widget.attrs.update({'class': 'form-control'})
    answer.widget.attrs.update({'class': 'form-control'})
    conviction.widget.attrs.update({'class': 'form-control'})

    
class DbQuestionsForm(forms.Form):
    question_id = forms.IntegerField(required='', label="Код")
    question = forms.CharField(required='', max_length=100, label="ФИО")

    question_id.widget.attrs.update({'class': 'form-control'})
    question.widget.attrs.update({'class': 'form-control'})

class DbDiseasesForm(forms.Form):
    diseases_id = forms.IntegerField(required='', label="Код")
    name = forms.CharField(required='', max_length=100, label="название")
    note = forms.CharField(required='', label="Пояснение")

    diseases_id.widget.attrs.update({'class': 'form-control'})
    name.widget.attrs.update({'class': 'form-control'})
    note.widget.attrs.update({'class': 'form-control'})
