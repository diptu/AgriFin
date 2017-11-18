# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrifin', '0006_farmer_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='NID',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='full_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(max_length=200, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='employee',
            name='qualification',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='NID',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='bank_credentials',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='profile_picture',
            field=models.ImageField(max_length=200, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='farmer',
            name='qualification',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='NID',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='bank_credentials',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='full_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='profile_picture',
            field=models.ImageField(max_length=200, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='investor',
            name='qualification',
            field=models.CharField(max_length=250, null=True),
        ),
    ]