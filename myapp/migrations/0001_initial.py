# Generated by Django 3.2.20 on 2023-07-12 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [ 
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('phone', models.CharField(max_length=16, verbose_name='电话')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
