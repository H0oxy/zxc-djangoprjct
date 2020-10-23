from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Board(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    prise = models.CharField(max_length=128)
    manufacturer = models.CharField(max_length=128)
    wide = models.CharField(max_length=128)
    length = models.CharField(max_length=128)
    material = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дека'
        verbose_name_plural = 'Деки'



class Wheel(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    prise = models.CharField(max_length=128)
    manufacturer = models.CharField(max_length=128)
    wheel_material = models.CharField(max_length=128)
    diameter = models.CharField(max_length=128)
    thickness = models.CharField(max_length=128)
    rigidity = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Колеса'
        verbose_name_plural = 'Колеса'


class Suspension(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    prise_rub = models.IntegerField(default=0)
    manufacturer = models.CharField(max_length=128)
    base_material =  models.CharField(max_length=128)
    axle = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подвеска'
        verbose_name_plural = 'Подвески'


class Spares(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    prise_rub = models.IntegerField(default=0)
    manufacturer = models.CharField(max_length=128)
    accuracy_class = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подшипники'
        verbose_name_plural = 'Подшипники'


