# Generated by Django 4.2.1 on 2023-06-26 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0022_remove_airline_stay_duration_order_stay_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stay_duration',
            field=models.IntegerField(default=0),
        ),
    ]