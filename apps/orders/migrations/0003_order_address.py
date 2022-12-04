# Generated by Django 4.0.6 on 2022-08-31 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_address_city'),
        ('orders', '0002_orderstatus_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.address', verbose_name='Адрес'),
        ),
    ]
