# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-15 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0022_populate_local_and_reply_and_share_counts'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='show_preview',
            field=models.BooleanField(default=True, help_text='Disable to turn off fetching and showing an OEmbed or OpenGraph preview using the links in the text.', verbose_name='Show OEmbed or OpenGraph preview'),
        ),
    ]
