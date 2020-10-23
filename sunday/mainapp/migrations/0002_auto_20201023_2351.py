# Generated by Django 2.2 on 2020-10-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spares',
            old_name='prise',
            new_name='prise_rub',
        ),
        migrations.RenameField(
            model_name='suspension',
            old_name='prise',
            new_name='prise_rub',
        ),
        migrations.RenameField(
            model_name='wheel',
            old_name='purpose',
            new_name='diameter',
        ),
        migrations.RemoveField(
            model_name='wheel',
            name='diameter_mm',
        ),
        migrations.AlterField(
            model_name='wheel',
            name='prise',
            field=models.CharField(max_length=128),
        ),
    ]