# Generated by Django 3.0.6 on 2020-07-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebKart', '0006_auto_20200715_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='1', upload_to='WebKart/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='2', upload_to='WebKart/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='3', upload_to='WebKart/images'),
        ),
    ]
