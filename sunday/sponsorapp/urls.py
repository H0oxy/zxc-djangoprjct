import sponsorapp.views as sponsorapp
from django.urls import path

app_name = 'sponsorapp'

urlpatterns = [
    path('sponsor/', sponsorapp.sponsor, name='sponsor'),

]
