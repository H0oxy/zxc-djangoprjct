# Generated by Django 2.2 on 2020-10-23 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_board'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': 'Дека', 'verbose_name_plural': 'Деки'},
        ),
        migrations.AlterModelOptions(
            name='suspension',
            options={'verbose_name': 'Подвеска', 'verbose_name_plural': 'Подвески'},
        ),
    ]
