import pdb
import datetime

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
from .models import Ancket
from .models import Question
from .models import Disease
from .models import Answer
from .models import Epicriz


from .forms import SigninForm
from .forms import RegisterForm
from .forms import DbPatientsForm
from .forms import DBAncketsForm
from .forms import DbQuestionsForm
from .forms import DbDiseasesForm
from .forms import PostuplenieForm
from .forms import ProfileForm
from .forms import DBEpicrizForm

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




def job_with_db_patients(request):

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





def db_questions(request, login):

    global g_login
    g_login = login
    
    db_questions_form = DbQuestionsForm()
    

    questions = Question.objects.all()

    context = {
        'login': login,
        'form': db_questions_form,
        'questions': questions,
    }
    template = "core/db_questions.html"
    return render(request, template, context)

def job_with_db_questions(request):
   
    if request.method == "POST":

        fields = {
            'question_id': request.POST.get("question_id"),
            'question': request.POST.get("question"),
        }
        
        if '_add' in request.POST:

            question = Question()

            if fields['question_id'] !='':
                question.id = fields['question_id']
            question.question = fields['question']

            question.save()


        #pdb.set_trace()
        if '_delete' in request.POST:
            if Question.objects.all().filter(id=fields['question_id']):
                Question.objects.all().filter(id=fields['question_id']).delete()
        else:
            return redirect('/doctor-' + g_login + '/db-questions/')

         


        #if '_change' in request.POST:


        return redirect('/doctor-' + g_login + '/db-questions/')

def db_diseases(request, login):

    global g_login
    g_login = login
    
    db_diseases_form = DbDiseasesForm()
    

    diseases = Disease.objects.all()

    context = {
        'login': login,
        'form': db_diseases_form,
        'diseases': diseases,
    }
    template = "core/db_diseases.html"
    return render(request, template, context)

def job_with_db_diseases(request):
   
    if request.method == "POST":

        fields = {
            'diseases_id': request.POST.get("diseases_id"),
            'name': request.POST.get("name"),
            'note': request.POST.get("note"),

        }
        
        if '_add' in request.POST:

            disease = Disease()

            if fields['diseases_id'] !='':
                disease.id = fields['diseases_id']
            disease.name = fields['name']
            disease.note = fields['note']


            disease.save()


        #pdb.set_trace()
        if '_delete' in request.POST:
            if Disease.objects.all().filter(id=fields['diseases_id']):
                Disease.objects.all().filter(id=fields['diseases_id']).delete()
        else:
            return redirect('/doctor-' + g_login + '/db-diseases/')

         


        #if '_change' in request.POST:


        return redirect('/doctor-' + g_login + '/db-diseases/')

# Страница "данные при поступлении"
def postuplenie(request, login):
    global g_login
    g_login = login
    
    postuplenie_form = PostuplenieForm()

    context = {
        'login': login,
        'form': postuplenie_form,
    }
    template = "core/postuplenie.html"
    return render(request, template, context)

# TODO: Удалить в следующиемм релизе, нигде не используется.    
def db_anckets(request, login, number_card):
    pdb.set_trace()

    if request.method == "POST":

        global g_login
        g_login = login

        db_anckets_form = DBAncketsForm()

        ankets = Ancket.objects.all() #Надо чтобы макеты выбирал по номеру карты а не все анкеты пациентов.

        context = {
            'login': login,
            'number_card': number_card,
            'form': db_anckets_form,
            'ankets': ankets,
        }
        template = "core/db_anckets.html"
        return render(request, template, context)


def chose_method_work_patient(request, login):
    if request.method == "POST":
        if 'opros_btn' in request.POST:
            return job_with_db_anckets(request)
        if 'epicriz_btn' in request.POST:   
            return job_with_db_epicriz(request, login)
        # if 'diagnoz_btn' in request.POST:   
        #     return job_with_db_epicriz(request)

def job_with_db_epicriz(request, login):
        # pdb.set_trace()
        # заход на сайт
        db_epicriz_form = DBEpicrizForm()
        epicrizis = Epicriz.objects.all()
        # pdb.set_trace()
        patient = Patient.objects.get(number_card = request.POST.get("number_card"))
        user = User.objects.get(login = login)
        if 'epicriz_btn' in request.POST:
            if Patient.objects.all().filter(number_card=request.POST.get("number_card")):
                db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
                epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            else:
                db_epicriz_form.fields["number_card"].initial = 'ОШИБКА: такой карты нет'
            # answers = Answer.objects.all().order_by('-date')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        # добавление нового эпикриза
        elif 'add_btn' in request.POST:
            db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
            is_invalid = False
            if request.POST.get("invalid"):
                is_invalid = True
            else:
                is_invalid = False
            # fields_add_epic = {
            #     'invalid': is_invalid,
            #     'lechenie': request.POST.get("lechenie"),
            #     'date_gospit': request.POST.get("date_gospit"),
            #     'lechenie': request.POST.get("date_vipisky"),
            # }
            epicriz = Epicriz()
            # pdb.set_trace()
            epicriz.patient = patient
            epicriz.user = user
            epicriz.invalid = is_invalid
            epicriz.lechenie = request.POST.get("lechenie")
            epicriz.date_gospit = request.POST.get("date_gospit")
            epicriz.date_vipisky = request.POST.get("date_vipisky")

            epicriz.save()

            epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        # удаление 
        elif 'delete_btn' in request.POST:
            epicriz = Epicriz()
            epicriz = Epicriz.objects.get(id = request.POST.get("number_epic"))
            epicriz.delete()
            
            db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
            epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        elif 'change_btn' in request.POST:
            db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
            is_invalid = False
            if request.POST.get("invalid"):
                is_invalid = True
            else:
                is_invalid = False
            # fields_add_epic = {
            #     'invalid': is_invalid,
            #     'lechenie': request.POST.get("lechenie"),
            #     'date_gospit': request.POST.get("date_gospit"),
            #     'lechenie': request.POST.get("date_vipisky"),
            # }
            epicriz = Epicriz.objects.get(id = request.POST.get("number_epic"))
            epicriz.patient = patient
            epicriz.user = user
            epicriz.invalid = is_invalid
            epicriz.lechenie = request.POST.get("lechenie")
            epicriz.date_gospit = request.POST.get("date_gospit")
            epicriz.date_vipisky = request.POST.get("date_vipisky")

            epicriz.save()

            epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        elif 'get_data_epic' in request.POST:
            db_epicriz_form.fields["number_card"].initial = request.POST.get("number_card")
            is_invalid = False
            if request.POST.get("invalid"):
                is_invalid = True
            else:
                is_invalid = False
            epicriz = Epicriz.objects.get(id = request.POST.get("number_epic"))
            db_epicriz_form.fields["number_epic"].initial = request.POST.get("number_epic")
            db_epicriz_form.fields["lechenie"].initial = epicriz.lechenie
            db_epicriz_form.fields["date_gospit"].initial = epicriz.date_gospit
            db_epicriz_form.fields["date_vipisky"].initial = epicriz.date_vipisky

            epicrizis = Epicriz.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date_gospit')
            context = {
                'login': login,
                'form': db_epicriz_form,
                'epicrizis': epicrizis,
                'patient': patient,
                'user': user,
            }
            template = "core/db_epicriz.html"
            return render(request, template, context)
        

def job_with_db_anckets(request):
    # pdb.set_trace()
    if request.method == "POST":
        # заход на сайт
        db_anckets_form = DBAncketsForm()
        ankets = Ancket.objects.all()
        
        if 'opros_btn' in request.POST:
            if Patient.objects.all().filter(number_card=request.POST.get("number_card")):
                db_anckets_form.fields["number_card"].initial = request.POST.get("number_card")
                ankets = Ancket.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date')
                # ankets.reverse()

            else:
                db_anckets_form.fields["number_card"].initial = 'ОШИБКА: такой карты нет'

            answers = Answer.objects.all().order_by('-date')
            context = {
                'login': request.POST.get("login"),
                'form': db_anckets_form,
                'ankets': ankets,
                'answers': answers,
            }
            template = "core/db_anckets.html"
            return render(request, template, context)
        # добавление новой анкеты
        elif 'add_opros' in request.POST:
            fields_add_opros = {
                'number_ancket': request.POST.get("number_ancket"),
                'number_card': request.POST.get("number_card"),
            }
            ancket = Ancket()
            
            some_patient = Patient.objects.get(number_card = fields_add_opros['number_card'])
            ancket.patient = some_patient
            ancket.date = datetime.datetime.now()
            ancket.save()

            db_anckets_form.fields["number_card"].initial = request.POST.get("number_card")

            ankets = Ancket.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date')
            # ankets.reverse()
            answers = Answer.objects.all().order_by('-date')
            context = {
                'login': request.POST.get("login"),
                'form': db_anckets_form,
                'ankets': ankets,
                'answers': answers,
            }
            template = "core/db_anckets.html"
            return render(request, template, context)
        # добавление ответа к выбранной анкете
        elif 'add_answer' in request.POST:
            fields_add_answer = {
                'number_ancket': request.POST.get("number_ancket"),
                'number_card': request.POST.get("number_card"),
                'question': request.POST.get("question"),
                'answer': request.POST.get("answer"),
                'conviction': request.POST.get("conviction"),
                
            }
            # pdb.set_trace()
            somevalue = fields_add_answer['number_ancket']
            ancket = Ancket.objects.get(id = fields_add_answer['number_ancket'])
            
            answer = Answer()
            answer.ancket = ancket
            answer.date = datetime.datetime.now()
            answer.note = fields_add_answer['answer']
            answer.question = Question.objects.get(question = fields_add_answer['question'])#fields_add_answer['question']
            answer.conviction = fields_add_answer['conviction']
            answer.save()

            db_anckets_form.fields["number_card"].initial = request.POST.get("number_card")
            db_anckets_form.fields["number_ancket"].initial = request.POST.get("number_ancket")


            ankets = Ancket.objects.filter(patient__number_card=request.POST.get("number_card")).order_by('-date')

            answers = Answer.objects.all().order_by('-date')
            context = {
                'login': request.POST.get("login"),
                'form': db_anckets_form,
                'ankets': ankets,
                'answers': answers,
            }
            template = "core/db_anckets.html"
            return render(request, template, context)
            
def profile(request,login):
    global g_login
    g_login = login

    profile_form = ProfileForm()
    # pdb.set_trace()
    user = User.objects.get(login = login)
    fields_save = {
            'login': "",
            'FIO': "",
            'postion': "",
            'department': "",
            'password': "",
        }

    if request.method == "POST":
            if 'save' in request.POST:
                fields_save = {
                    'login': request.POST.get("login"),
                    'FIO': request.POST.get("FIO"),
                    'postion': request.POST.get("postion"),
                    'department': request.POST.get("department"),
                    'password': request.POST.get("password"),
                }
                user = User.objects.get(login = login)
                user.FIO = fields_save['FIO']
                if User.objects.all().filter(login = fields_save['login']):
                    donothing = 0
                else:
                    user.login = fields_save['login']
                user.Postion = fields_save['postion']
                user.Department = fields_save['department']
                user.password = fields_save['password']
                
                user.save()

    # pdb.set_trace()
    template = "core/profile.html"

    profile_form = ProfileForm()
    profile_form.fields['FIO'].initial = user.FIO
    profile_form.fields['login'].initial = user.login
    profile_form.fields['postion'].initial = user.Postion
    profile_form.fields['department'].initial = user.Department
    profile_form.fields['password'].initial = user.password

    context = {
        'login': login,
        'form': profile_form,
        }
    return render(request, template, context)