# Generated by Django 4.0.6 on 2022-07-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormWholesaler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=30, verbose_name='Email')),
                ('company_name', models.CharField(blank=True, max_length=50, verbose_name='Название компании')),
                ('social_network', models.CharField(blank=True, max_length=50, verbose_name='Вебсайт/Instagram')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Город')),
                ('document', models.FileField(blank=True, help_text='Документ для ускорения модерации', upload_to='files/documents', verbose_name='Сертификат/Диплом')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий/Вопросы')),
            ],
            options={
                'verbose_name': 'Заявка от оптовика',
                'verbose_name_plural': 'Заявки от оптовиков',
                'db_table': 'forms_wholesalers',
            },
        ),
    ]
