# Generated by Django 4.0.6 on 2022-07-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dosage',
            field=models.CharField(blank=True, max_length=50, verbose_name='Дозировка'),
        ),
    ]
