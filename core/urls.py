from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [

    path('', views.base_core, name="base_core"),
    path('sign-in/', views.sign_in, name="sign_in"),
    path('register/', views.register, name="register"),
    path('main/', views.main, name="main"),

]