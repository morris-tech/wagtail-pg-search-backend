# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-22 14:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.CharField(blank=True, max_length=63)),
                ('object_id', models.TextField()),
                ('title', models.TextField()),
                ('body', models.TextField(blank=True)),
                ('body_search', django.contrib.postgres.search.SearchVectorField()),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'index entries',
                'verbose_name': 'index entry',
            },
        ),
        migrations.AlterUniqueTogether(
            name='indexentry',
            unique_together=set([('config', 'content_type', 'object_id')]),
        ),
    ]