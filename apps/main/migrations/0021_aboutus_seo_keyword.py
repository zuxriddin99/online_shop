# Generated by Django 4.0.6 on 2022-11-28 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_ourblog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='seo_keyword',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]