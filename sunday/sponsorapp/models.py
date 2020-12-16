from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спонсор'
        verbose_name_plural = 'Спонсоры'