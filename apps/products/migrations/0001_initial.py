# Generated by Django 4.0.6 on 2022-07-15 12:30

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название бренда')),
                ('slug', models.SlugField(blank=True, max_length=105, unique=True, verbose_name='Slug')),
                ('logo', models.ImageField(upload_to='images/brand/', verbose_name='Логотип бренда')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание бренда')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, max_length=105, unique=True, verbose_name='Slug')),
                ('icon', models.ImageField(upload_to='images/category/', verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=205, unique=True, verbose_name='Slug')),
                ('quantity_in_stock', models.IntegerField(default=0, verbose_name='Количество на складе')),
                ('short_desc', models.CharField(blank=True, max_length=250, verbose_name='Краткое описание товара')),
                ('full_desc', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Полное описание товара')),
                ('publication_status', models.CharField(choices=[('moderation', 'На модерации'), ('published', 'Опубликовано'), ('draft', 'Черновик')], default='published', max_length=50, verbose_name='Статус публикации')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время создания публикации')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания публикации')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand', verbose_name='Бред')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_quantity', models.PositiveSmallIntegerField(null=True, verbose_name='Цена товара от количество')),
                ('price', models.DecimalField(decimal_places=0, max_digits=12, verbose_name='Цена')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Цена товара',
                'verbose_name_plural': 'Цены товара',
                'db_table': 'products_prices',
                'ordering': ('-from_quantity',),
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images/product/', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'db_table': 'products_images',
            },
        ),
    ]
