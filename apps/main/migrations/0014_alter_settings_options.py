# Generated by Django 4.0.6 on 2022-10-31 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_settings_admin_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Настройка сайта', 'verbose_name_plural': 'Настройки сайта'},
        ),
    ]
