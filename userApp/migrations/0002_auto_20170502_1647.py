# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('group', models.ForeignKey(to='userApp.Group')),
            ],
            options={
                'db_table': 'resource_groups_permission',
            },
        ),
        migrations.CreateModel(
            name='ResourcePermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('action_type', models.ForeignKey(to='userApp.ActionType')),
            ],
            options={
                'db_table': 'resource_permissions',
            },
        ),
        migrations.RemoveField(
            model_name='resourcegroup',
            name='group',
        ),
        migrations.RemoveField(
            model_name='resourcegroup',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='action_type',
        ),
        migrations.AlterModelTable(
            name='resource',
            table='resources',
        ),
        migrations.DeleteModel(
            name='ResourceGroup',
        ),
        migrations.AddField(
            model_name='resourcepermission',
            name='resource',
            field=models.ForeignKey(to='userApp.Resource'),
        ),
        migrations.AddField(
            model_name='resourcegrouppermissions',
            name='resource_perm',
            field=models.ForeignKey(to='userApp.ResourcePermission'),
        ),
    ]
