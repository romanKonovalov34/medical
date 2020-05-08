from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    age = models.CharField(max_length=3, verbose_name='Возраст')
    login = models.CharField(max_length = 50, verbose_name='Логин')
    password = models.CharField(max_length = 50, verbose_name='Пароль')



    def __str__(self):
        return self.name



    class Meta():
        verbose_name = 'пользователя'
        verbose_name_plural='пользователи'