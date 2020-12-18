from django.db import models

class Week(models.Model):
    day_of_the_week = models.CharField(max_length=128)
    desc = models.TextField(blank=True)


    def __str__(self):
        return self.day_of_the_week

    class Meta:
        verbose_name = 'Неделя'
        verbose_name_plural = 'Недели'