# Generated by Django 4.0.6 on 2022-07-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_usersmscode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(help_text='Без +', max_length=15, unique=True, verbose_name='Номер телефона'),
        ),
    ]
