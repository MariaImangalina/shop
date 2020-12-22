# Generated by Django 3.0.6 on 2020-12-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200921_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_options',
            field=models.CharField(blank=True, choices=[('Courier', 'Courier'), ('Pickup', 'Pickup')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickup_point',
            field=models.CharField(blank=True, choices=[('MSU', 'MSU'), ('Cosmos_Hotel', 'Cosmos_Hotel'), ('Gorod_Mall', 'Gorod_Mall')], max_length=150, null=True),
        ),
    ]
