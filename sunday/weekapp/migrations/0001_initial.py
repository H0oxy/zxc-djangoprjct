# Generated by Django 2.2 on 2020-12-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_the_week', models.CharField(max_length=128)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Неделя',
                'verbose_name_plural': 'Недели',
            },
        ),
    ]