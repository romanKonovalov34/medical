from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages



from .models import User
#from .models import Doctor
from .models import Patient

from .forms import SigninForm
from .forms import RegisterForm
from .forms import DbPatientsForm


# Create your views here.

g_login = ''

def base_core(request):
    signin_form = SigninForm()
    template = "core/base_core.html"
    return render(request, template, {"form": signin_form})




def sign_in(request):
    if request.method == "POST":
        user = User()

        fields = {
            'login': request.POST.get("login"),
            'password': request.POST.get("password"),
        }

        if User.objects.all().filter(login=fields['login']):
            user.login = fields['login']
            user.password = fields['password']
            #user.save()
            #return HttpResponseRedirect('/main')
            template = 'core/main.html'
            return render(request, template, {"login": user.login})
            #return HttpResponseRedirect(reverse("main", kwargs={'login': user.login}))

        else:
            signin_form = SigninForm()
            template = "core/base_core.html"
            return render(request, template, {"form": signin_form, "message": "Данные введены не корректно"})
            
    else:
        signin_form = SigninForm()
        template = "core/sign_in.html"
        return render(request, template, {"form": signin_form})





def register(request):
    if request.method == "POST":
        user = User()

        fields = {
            'login': request.POST.get("login"),
            'password': request.POST.get("password"),
            'rePassword': request.POST.get("rePassword")
        }

        if User.objects.all().filter(login=fields['login']):
            reg_form = RegisterForm()
            template = "core/register.html"
            return render(request, template, {"form": reg_form, "message":"Пользователь с таким логином уже зарегистрирован"})

        elif fields['password'] != fields['rePassword']:
            reg_form = RegisterForm()
            template = "core/register.html"
            return render(request, template, {"form": reg_form, "message": "Введенные пароли не совпадают. Попробуйте еще раз"})

        else:
            user.login = fields['login']
            user.password = fields['password']
            user.isAdmin = False
            user.save()
            return HttpResponseRedirect('/sign-in/')
    else:
        reg_form = RegisterForm()
        template = "core/register.html"
        return render(request, template, {"form": reg_form})



#def main(request):
#    users = User.objects.all()

#    context = {
#        'users': users,
#    }

#    template = "core/main.html"
#    return render(request, template, context)




def main(request):
    if request.method == "POST":
        user = User()

        fields = {
            'login': request.POST.get("login"),
            'password': request.POST.get("password"),
            # возвращает 'none' или 'on'
            'isAdmin': request.POST.get("isAdmin"),
        }

        if User.objects.all().filter(login=fields['login']):
            #user.login = fields['login']
            #user.password = fields['password']
            template = 'core/main.html'
            return render(request, template, {"login": fields["login"]})

        else:
            signin_form = SigninForm()
            template = "core/base_core.html"
            return render(request, template, {"form": signin_form, "message": "Пользователь с таким логином не зарегистрирован"})
        
    else:
        return redirect('/')



def db_patients(request, login):

    global g_login
    g_login = login

    #if request.method == "POST":
    #    patient = Patient()

    #    fields = {
    #        'number_card': request.POST.get("number_card"),
    #        'FIO': request.POST.get("FIO"),
    #        'date_birth': request.POST.get("date_birth"),
    #        'nationality': request.POST.get("nationality"),
    #        'education': request.POST.get("education"),
    #        'address': request.POST.get("address"),
    #        'job': request.POST.get("job"),
    #        'position': request.POST.get("position"),
    #    }

    #    if Patient.objects.all().filter(number_card=fields['number_card']):
    #        return redirect('/')
        
    #else:
    db_patients_form = DbPatientsForm()


    patients = Patient.objects.all()

    context = {
        'login': login,
        'form': db_patients_form,
        'patients': patients,
    }
    template = "core/db_patients.html"
    return render(request, template, context)




def job_with_db(request):

    if request.method == "POST":

        fields = {
            'number_card': request.POST.get("number_card"),
            'FIO': request.POST.get("FIO"),
            'date_birth': request.POST.get("date_birth"),
            'sex': request.POST.get("sex"),
            'nationality': request.POST.get("nationality"),
            'education': request.POST.get("education"),
            'address': request.POST.get("address"),
            'phone': request.POST.get("phone"),
            'job': request.POST.get("job"),
            'position': request.POST.get("position"),
        }



        if '_add' in request.POST:

            patient = Patient()

            patient.number_card = fields['number_card']
            patient.FIO = fields['FIO']
            patient.date_birth = fields['date_birth']
            patient.sex = fields['sex']
            patient.nationality = fields['nationality']
            patient.education = fields['education']
            patient.address = fields['address']
            patient.phone = fields['phone']
            patient.job = fields['job']
            patient.position = fields['position']

            patient.save()



        if '_delete' in request.POST:
            if Patient.objects.all().filter(number_card=fields['number_card']):
                Patient.objects.all().filter(number_card=fields['number_card']).delete()
        else:
            return redirect('/doctor-' + g_login + '/db-patients/')

         


        #if '_change' in request.POST:





        return redirect('/doctor-' + g_login + '/db-patients/')















def delete_patient(request):

    if request.method == "POST":

        fields = {
            'number_card': request.POST.get("number_card"),
            'FIO': request.POST.get("FIO"),
            'date_birth': request.POST.get("date_birth"),
            'sex': request.POST.get("sex"),
            'nationality': request.POST.get("nationality"),
            'education': request.POST.get("education"),
            'address': request.POST.get("address"),
            'phone': request.POST.get("phone"),
            'job': request.POST.get("job"),
            'position': request.POST.get("position"),
        }

        patient = Patient()

        patient.number_card = fields['number_card']
        patient.FIO = fields['FIO']
        patient.date_birth = fields['date_birth']
        patient.sex = fields['sex']
        patient.nationality = fields['nationality']
        patient.education = fields['education']
        patient.address = fields['address']
        patient.phone = fields['phone']
        patient.job = fields['job']
        patient.position = fields['position']

        patient.save()

    return redirect('/doctor-' + g_login + '/db-patients/')


def change_patient(request):

    if request.method == "POST":

        fields = {
            'number_card': request.POST.get("number_card"),
            'FIO': request.POST.get("FIO"),
            'date_birth': request.POST.get("date_birth"),
            'sex': request.POST.get("sex"),
            'nationality': request.POST.get("nationality"),
            'education': request.POST.get("education"),
            'address': request.POST.get("address"),
            'phone': request.POST.get("phone"),
            'job': request.POST.get("job"),
            'position': request.POST.get("position"),
        }

        patient = Patient()

        patient.number_card = fields['number_card']
        patient.FIO = fields['FIO']
        patient.date_birth = fields['date_birth']
        patient.sex = fields['sex']
        patient.nationality = fields['nationality']
        patient.education = fields['education']
        patient.address = fields['address']
        patient.phone = fields['phone']
        patient.job = fields['job']
        patient.position = fields['position']

        patient.save()

    return redirect('/doctor-' + g_login + '/db-patients/')



# Страница "данные при поступлении"
def postuplenie(request, login):

    global g_login
    g_login = login

    db_patients_form = DbPatientsForm()


    patients = Patient.objects.all()

    context = {
        'login': login,
        'form': db_patients_form,
        'patients': patients,
    }
    template = "core/postuplenie.html"
    return render(request, template, context)