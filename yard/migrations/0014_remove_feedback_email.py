# Generated by Django 3.1.7 on 2021-04-01 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yard', '0013_auto_20210330_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='email',
        ),
    ]
