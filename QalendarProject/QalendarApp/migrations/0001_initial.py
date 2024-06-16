# Generated by Django 5.0.6 on 2024-06-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('time_constraint', models.CharField(max_length=4)),
                ('preference', models.CharField(default='None', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('day', models.IntegerField()),
                ('start_time', models.CharField(max_length=4)),
                ('end_time', models.CharField(max_length=4)),
            ],
        ),
    ]
