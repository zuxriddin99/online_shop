# Generated by Django 4.0.6 on 2022-07-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formwholesaler',
            name='business_type',
            field=models.CharField(choices=[('Для себя', 'Для себя'), ('Продажа', 'Продажа'), ('Другое', 'Другое')], default='Другое', max_length=50, verbose_name='Тип бизнеса'),
        ),
    ]