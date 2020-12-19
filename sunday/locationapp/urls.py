import locationapp.views as locationapp
from django.urls import path

app_name = 'locationapp'

urlpatterns = [
    path('location/', locationapp.location, name='location'),

]
