# Generated by Django 3.1.7 on 2021-04-16 01:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0015_auto_20210416_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='following_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('to_id', models.IntegerField()),
                ('fro_id', models.IntegerField()),
            ],
        ),
    ]
