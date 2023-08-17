# Generated by Django 4.1.1 on 2022-10-30 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_airport', models.CharField(max_length=100)),
                ('destination_airport', models.CharField(max_length=100)),
                ('airlines', models.CharField(choices=[('中国国航', '中国国航'), ('昆明航空', '昆明航空'), ('深圳航空', '深圳航空'), ('海南航空', '海南航空')], max_length=100)),
                ('flight', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]