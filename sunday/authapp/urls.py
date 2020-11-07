import authapp.views as authapp
from django.contrib import admin
from django.urls import path

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
]
