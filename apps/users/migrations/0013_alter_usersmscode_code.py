# Generated by Django 4.0.6 on 2022-10-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmscode',
            name='code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Код из смс'),
        ),
    ]