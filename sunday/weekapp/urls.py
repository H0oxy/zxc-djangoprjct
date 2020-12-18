import weekapp.views as weekapp
from django.urls import path

app_name = 'weekapp'

urlpatterns = [
    path('week/', weekapp.week, name='week'),

]
