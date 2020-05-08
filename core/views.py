from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages



from .models import User
from .forms import SigninForm
from .forms import RegisterForm


# Create your views here.



def base_core(request):
    if request.method == "POST":
        user = User()

        fields = {
            'login': request.POST.get("login"),
            'password': request.POST.get("password"),
        }

        if User.objects.all().filter(login=fields['login']):
            user.login = fields['login']
            user.password = fields['password']
            user.save()
            return HttpResponseRedirect("/main/")

        else:
            signin_form = SigninForm()
            template = "core/base_core.html"
            return render(request, template, {"form": signin_form, "message": "Пользователь с таким логином не зарегистрирован"})

    else:
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
            user.save()
            return HttpResponseRedirect('/main/')

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
            user.save()
            return HttpResponseRedirect('/sign-in/')
    else:
        reg_form = RegisterForm()
        template = "core/register.html"
        return render(request, template, {"form": reg_form})



def main(request):
    users = User.objects.all()

    context = {
        'users': users,
    }

    template = "core/main.html"
    return render(request, template, context)

