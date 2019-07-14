# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-07-14 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0005_auto_20190714_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '未报名'), (1, '已报名')], default=0),
        ),
        migrations.AlterField(
            model_name='customerfollowup',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.UserProfile', verbose_name='跟进人'),
        ),
        migrations.AlterField(
            model_name='customerfollowup',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.Customer', verbose_name='潜在学员'),
        ),
        migrations.AlterField(
            model_name='customerfollowup',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='跟进日期'),
        ),
        migrations.AlterField(
            model_name='customerfollowup',
            name='intention',
            field=models.SmallIntegerField(choices=[(0, '2周内报名'), (1, '一个月内报名'), (2, '近期无报名计划'), (3, '已在其他机构报名'), (4, '已报名'), (5, '已拉黑')], verbose_name='跟进结果'),
        ),
    ]