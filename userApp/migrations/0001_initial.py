# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('user_name', models.CharField(unique=True, max_length=200)),
                ('phone_no', models.CharField(default=b'', max_length=20, null=True, db_index=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'action_types',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, unique=True, null=True, blank=True)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('url', models.CharField(default=b'', max_length=200, unique=True, null=True, blank=True)),
                ('action_type', models.ForeignKey(to='userApp.ActionType')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('group', models.ForeignKey(to='userApp.Group')),
                ('resource', models.ForeignKey(to='userApp.Resource')),
            ],
            options={
                'db_table': 'resource_groups',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('group', models.ForeignKey(to='userApp.Group')),
                ('user', models.ForeignKey(to='userApp.User')),
            ],
            options={
                'db_table': 'user_groups',
            },
        ),
    ]
