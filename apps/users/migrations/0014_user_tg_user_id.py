# Generated by Django 4.0.6 on 2022-11-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_usersmscode_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
