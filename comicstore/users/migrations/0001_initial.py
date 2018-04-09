# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userparty',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('isdelete', models.BooleanField(default=False, verbose_name='删除时间')),
                ('creatime', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updatetime', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('username', models.CharField(verbose_name='姓名', max_length=20)),
                ('password', models.CharField(verbose_name='密码', max_length=40)),
                ('email', models.EmailField(verbose_name='邮箱地址', max_length=254)),
                ('is_active', models.BooleanField(default=False, verbose_name='激活状态')),
            ],
            options={
                'db_table': 'usertable',
            },
        ),
    ]
