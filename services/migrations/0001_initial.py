# Generated by Django 3.0.7 on 2020-09-22 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('teaser', models.CharField(default='milad', max_length=200)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos')),
                ('is_published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
