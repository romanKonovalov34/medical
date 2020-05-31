from django.db import models

# Create your models here.





class User(models.Model):
    login = models.CharField(max_length=200, verbose_name='Логин')
    password = models.CharField(max_length = 50, verbose_name='Пароль')
    isAdmin = models.BooleanField(verbose_name='Я администратор') # Не нужно, но пусть будет чтобы ошибок не было.
    FIO = models.CharField(max_length = 50, verbose_name='ФИО', default="")
    Postion = models.CharField(max_length = 50, verbose_name='Позиция', default="")
    Department = models.CharField(max_length = 50, verbose_name='Отделение', default="")

    def __str__(self):
        return self.login


    class Meta():
        verbose_name = 'пользователя'
        verbose_name_plural='пользователи'




class Patient(models.Model):
    number_card = models.IntegerField(verbose_name="Номер карты")
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
        return self.number_card


    class Meta():
        verbose_name = 'пациента'
        verbose_name_plural='пациенты'

# Сущность анкета пациента
class Ancket(models.Model):
    date = models.CharField(max_length=100, verbose_name="Дата анкеты")
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, verbose_name="Пациент")

    def __str__(self):
        return self.date


    class Meta():
        verbose_name = 'анкета'
        verbose_name_plural='анкеты'

# Вопросы
class Question(models.Model):
    question = models.CharField(max_length=100, verbose_name="Вопрос")

    def __str__(self):
        return self.question


    class Meta():
        verbose_name = 'вопрос'
        verbose_name_plural='вопросы'

# ответы
class Answer(models.Model):
    date = models.DateField()
    note = models.TextField()
    conviction = models.IntegerField(default=0)
    ancket = models.ForeignKey(Ancket, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.note


    class Meta():
        verbose_name = 'ответ'
        verbose_name_plural='ответы'

# Болезни(диагнозы)
class Disease(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    note = models.TextField() #описание

    def __str__(self):
        return self.name


    class Meta():
        verbose_name = 'болезнь'
        verbose_name_plural='болезни'

# Эпикризы
class Epicriz(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    invalid = models.BooleanField(default = False)
    lechenie = models.CharField(max_length=500, default="", verbose_name="Лечение", null=True)
    date_gospit = models.DateField(default = "1999-01-01" , null=True)
    date_vipisky = models.DateField(default = "1999-01-01", null=True)

    def __str__(self):
        return self.lechenie


    class Meta():
        verbose_name = 'эпикриз'
        verbose_name_plural='эпикризы'


# Диагнозы
class Diagnos(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    epicriz = models.ForeignKey(Epicriz, on_delete = models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete = models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return self.note


    class Meta():
        verbose_name = 'диагноз'
        verbose_name_plural='диагнозы'