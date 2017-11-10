# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=500)),
                ('number_of_employee', models.DecimalField(decimal_places=0, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.DecimalField(decimal_places=2, max_digits=20)),
                ('fartility_rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('location', models.CharField(max_length=500)),
                ('share_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('share_quantity', models.DecimalField(decimal_places=0, max_digits=5)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgriFinance.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=250)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('profile_picture', models.ImageField(max_length=200, upload_to=b'')),
                ('NID', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_bought', models.DecimalField(decimal_places=2, max_digits=3)),
                ('land_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgriFinance.Land')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AgriFinance.Person')),
                ('user_name', models.CharField(max_length=50)),
                ('NID', models.CharField(max_length=50)),
                ('branch_id', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AgriFinance.Person')),
                ('user_name', models.CharField(max_length=50)),
                ('NID', models.CharField(max_length=50)),
                ('bank_credentials', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AgriFinance.Person')),
                ('user_name', models.CharField(max_length=50)),
                ('NID', models.CharField(max_length=50)),
                ('bank_credentials', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='land',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgriFinance.Person'),
        ),
        migrations.AddField(
            model_name='share',
            name='investor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgriFinance.Investor'),
        ),
        migrations.AlterUniqueTogether(
            name='share',
            unique_together=set([('land_id', 'investor_id')]),
        ),
    ]
