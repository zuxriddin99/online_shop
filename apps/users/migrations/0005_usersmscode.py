# Generated by Django 4.0.6 on 2022-07-23 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usercartitem_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSMSCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SmallIntegerField(verbose_name='Код из смс')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время отправленного смс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Код из смс',
                'verbose_name_plural': 'Коды из смс-ок',
                'db_table': 'users_codes',
            },
        ),
    ]
