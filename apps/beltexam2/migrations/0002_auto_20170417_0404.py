# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beltexam2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='poked',
            field=models.ManyToManyField(blank=True, related_name='poked_by', to='beltexam2.User'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked_key', to='beltexam2.User'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poker_key', to='beltexam2.User'),
        ),
    ]
