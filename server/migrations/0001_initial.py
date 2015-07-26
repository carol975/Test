# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=30)),
                ('project_summary', models.CharField(max_length=500)),
                ('date_created', models.DateField()),
                ('image_path', models.CharField(default=None, max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_name', models.CharField(max_length=30)),
                ('projects', models.ManyToManyField(to='server.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_summary', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=30)),
                ('image_path', models.CharField(default=None, max_length=50, null=True, blank=True)),
                ('owner', models.ForeignKey(related_name='server', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='types',
            name='users',
            field=models.ManyToManyField(to='server.UserProfiles'),
        ),
        migrations.AddField(
            model_name='skills',
            name='users',
            field=models.ManyToManyField(to='server.UserProfiles'),
        ),
        migrations.AddField(
            model_name='projects',
            name='id_owner',
            field=models.ForeignKey(to='server.UserProfiles'),
        ),
        migrations.AddField(
            model_name='projects',
            name='id_types',
            field=models.ForeignKey(to='server.Types'),
        ),
    ]
