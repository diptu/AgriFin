# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrifin', '0004_land'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_bought', models.DecimalField(decimal_places=2, max_digits=3)),
                ('investor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrifin.Investor')),
                ('land_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrifin.Land')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='share',
            unique_together=set([('land_id', 'investor_id')]),
        ),
    ]
