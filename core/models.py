from django.db import models

# Create your models here.





class User(models.Model):
    login = models.CharField(max_length=200, verbose_name='ФИО')
    password = models.CharField(max_length = 50, verbose_name='Пароль')
    isAdmin = models.BooleanField(verbose_name='Я администратор')


    def __str__(self):
        return self.name


    class Meta():
        verbose_name = 'пользователя'
        verbose_name_plural='пользователи'






#class Doctor(models.Model):
#    name = models.CharField(max_length=200, verbose_name='ФИО')
#    age = models.CharField(max_length=3, verbose_name='Возраст')
#    login = models.CharField(max_length = 50, verbose_name='Логин')
#    password = models.CharField(max_length = 50, verbose_name='Пароль')


#    def __str__(self):
#        return self.name


#    class Meta():
#        verbose_name = 'Доктора'
#        verbose_name_plural='Доктора'






class Patient(models.Model):
    number_card = models.IntegerField(max_length=50, verbose_name="Номер карты")
    FIO = models.CharField(max_length=100, verbose_name="ФИО")
    date_birth = models.CharField(max_length=100, verbose_name="Дата рождения")
    sex = models.CharField(max_length=50, verbose_name="Пол")
    nationality = models.CharField(max_length=50, verbose_name="Национальность")
    education = models.CharField(max_length=100, verbose_name="Образование")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    job = models.CharField(max_length=100, verbose_name="Место работы")
    position = models.CharField(max_length=100, verbose_name="Должность")


    def __str__(self):
        return self.name


    class Meta():
        verbose_name = 'пациента'
        verbose_name_plural='пациенты'