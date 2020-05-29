from django.contrib import admin
from django.urls import path, re_path
from core import views


urlpatterns = [
    path('', views.base_core, name="base_core"),
    path('sign-in/', views.sign_in, name="sign_in"),
    path('register/', views.register, name="register"),
    path('main/', views.main, name="main"),
    path('doctor-<login>/db-patients/', views.db_patients, name="db_patients"),
    path('job-with-db-patients/', views.job_with_db_patients, name="job_with_db_patients"),
    path('doctor-<login>/postuplenie/', views.postuplenie, name="postuplenie"),
    path('doctor-<login>/postuplenie/add-form', views.add_form, name="add_form"),
    path('doctor-<login>/db-questions/', views.db_questions, name="db_questions"),
    path('job-with-db-questions/', views.job_with_db_questions, name="job_with_db_questions"),

]