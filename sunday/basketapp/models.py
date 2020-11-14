from django.contrib.auth.modeles import User
from django.db import models

from mainapp.modeles import Board


class BoardBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Board,  on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
