# Generated by Django 3.0.6 on 2020-09-21 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20200903_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='weight',
        ),
    ]
