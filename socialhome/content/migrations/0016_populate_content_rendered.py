# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 19:19
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations
from django.db.migrations import RunPython


def forward(apps, schema_editor):
    # Removed as it's causing exceptions and is not needed except for old nodes
    # which should have updated by now
    # call_command("runscript", "0016_populate_content_rendered")
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_remove_tag_modified'),
    ]

    operations = [
        RunPython(RunPython.noop, RunPython.noop),
    ]
