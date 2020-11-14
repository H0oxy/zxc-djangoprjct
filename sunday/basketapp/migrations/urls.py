import authapp.views as authapp
from django.contrib import admin
from django.urls import path

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.login, name='logout'),
    path('register/', authapp.register, name='register'),
]
