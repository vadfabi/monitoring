# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Пулы',
                'verbose_name': 'Пул',
            },
        ),
        migrations.CreateModel(
            name='UserPools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('claymore_port', models.IntegerField(default=3333)),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.Pools')),
            ],
            options={
                'verbose_name_plural': 'Кошельки на пуле',
                'verbose_name': 'Кошелёк на пуле',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_submit_time', models.DateTimeField(null=True)),
                ('reported_hash_rate', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('valid_shares', models.IntegerField(null=True)),
                ('invalid_shares', models.IntegerField(null=True)),
                ('stale_shares', models.IntegerField(null=True)),
                ('invalid_share_ratio', models.IntegerField(null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('uptime', models.BigIntegerField(default=0, null=True)),
                ('ip_address', models.CharField(max_length=255, null=True)),
                ('sum_hr_base', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('sum_hr_sec', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('hr_details_base', models.CharField(max_length=255, null=True)),
                ('hr_details_sec', models.CharField(max_length=255, null=True)),
                ('temperature', models.CharField(max_length=255, null=True)),
                ('fun_speed', models.CharField(max_length=255, null=True)),
                ('pools', models.CharField(max_length=255, null=True)),
                ('claymore_version', models.CharField(max_length=255, null=True)),
                ('claymore_uptime', models.BigIntegerField(default=0, null=True)),
                ('address_pool', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring.UserPools')),
            ],
        ),
        migrations.CreateModel(
            name='WorkersHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_hash_rate', models.DecimalField(decimal_places=1, max_digits=5)),
                ('date_time', models.DateTimeField()),
                ('sum_hr_base', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('sum_hr_sec', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.Worker')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='worker',
            unique_together=set([('address_pool', 'name')]),
        ),
    ]