from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'