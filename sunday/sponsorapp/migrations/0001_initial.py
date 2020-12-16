# Generated by Django 2.2 on 2020-12-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Спонсор',
                'verbose_name_plural': 'Спонсоры',
            },
        ),
    ]
