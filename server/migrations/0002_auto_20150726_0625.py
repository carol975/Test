# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='id_owner',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='id_types',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='users',
        ),
        migrations.RemoveField(
            model_name='types',
            name='users',
        ),
        migrations.RemoveField(
            model_name='userprofiles',
            name='owner',
        ),
        migrations.AddField(
            model_name='skills',
            name='users_profiles',
            field=models.ManyToManyField(related_name='skills', to='server.UserProfiles'),
        ),
        migrations.AddField(
            model_name='types',
            name='projects',
            field=models.ManyToManyField(related_name='types', to='server.Projects'),
        ),
        migrations.AddField(
            model_name='types',
            name='user_profiles',
            field=models.ManyToManyField(related_name='types', to='server.UserProfiles'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='date_created',
            field=models.DateField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='projects',
            field=models.ManyToManyField(related_name='skills', to='server.Projects'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
