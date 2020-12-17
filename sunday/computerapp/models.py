from django.db import models

class Computer(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    videocard = models.CharField(max_length=128)
    ram = models.CharField(max_length=128)
    cpu = models.CharField(max_length=128)
    mother_board = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'