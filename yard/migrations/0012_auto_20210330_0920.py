# Generated by Django 3.1.7 on 2021-03-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0011_auto_20210330_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='prefix_filter',
            field=models.CharField(blank=True, max_length=3, verbose_name='Префикс для фильтра'),
        ),
        migrations.AlterField(
            model_name='sphere',
            name='prefix',
            field=models.CharField(blank=True, max_length=3, verbose_name='Префикс'),
        ),
    ]
