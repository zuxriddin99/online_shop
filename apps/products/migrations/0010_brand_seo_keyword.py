# Generated by Django 4.0.6 on 2022-11-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_brand_description_alter_brand_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='seo_keyword',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
