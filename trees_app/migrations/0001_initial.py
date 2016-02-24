# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('scientific_name', models.CharField(max_length=40)),
                ('wood', models.CharField(choices=[('hard', 'Hardwood'), ('soft', 'Softwood')], max_length=10)),
                ('type_tree', models.CharField(choices=[('dec', 'Deciduous'), ('con', 'Coniferous')], max_length=10)),
                ('max_height', models.IntegerField()),
                ('location', models.CharField(max_length=15)),
                ('uses', models.CharField(max_length=50)),
            ],
        ),
    ]