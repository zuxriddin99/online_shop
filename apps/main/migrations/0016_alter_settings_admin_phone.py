# Generated by Django 4.0.6 on 2022-10-31 13:23

import apps.main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_formwholesaler_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='admin_phone',
            field=models.CharField(max_length=9, null=True, validators=[apps.main.models.phone_number_validation], verbose_name='Введите номер без +'),
        ),
    ]
