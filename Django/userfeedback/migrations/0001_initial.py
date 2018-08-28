# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-27 10:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('neighbourhood', models.CharField(choices=[('WESTLANDS', 'Westlands'), ('EASTLEIGH', 'Eastleigh'), ('UPPER HILL', 'Upper Hill'), ('LAVINGTON', 'Lavington'), ('NAIROBI WEST', 'Nairobi West')], max_length=100)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]