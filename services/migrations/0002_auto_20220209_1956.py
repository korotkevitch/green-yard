# Generated by Django 3.1.7 on 2022-02-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetail',
            name='image_main',
            field=models.FileField(blank=True, upload_to='services', verbose_name='Фото на Главной 600*500'),
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='slogan',
            field=models.CharField(blank=True, max_length=30, verbose_name='Слоган после заголовка'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='text_1',
            field=models.CharField(blank=True, max_length=5000, verbose_name='Первый текст'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='text_2',
            field=models.CharField(blank=True, max_length=5000, verbose_name='Второй текст'),
        ),
    ]
