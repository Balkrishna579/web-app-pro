# Generated by Django 3.1.7 on 2021-04-13 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0007_auto_20210413_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='follow_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('to_id', models.IntegerField()),
                ('fro_id', models.IntegerField()),
            ],
        ),
    ]