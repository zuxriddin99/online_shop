# Generated by Django 4.0.6 on 2022-11-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_settings_admin_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(default=1, upload_to='images/aboutus/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='keyword',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
