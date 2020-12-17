import computerapp.views as computerapp
from django.urls import path

app_name = 'computerapp'

urlpatterns = [
    path('computer/', computerapp.computer, name='computer'),

]
