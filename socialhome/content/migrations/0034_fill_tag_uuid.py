# Generated by Django 2.0.8 on 2019-02-15 23:23
import uuid

from django.db import migrations
from django.db.migrations import RunPython


def forward(apps, schema_editor):
    Tag = apps.get_model("content", "Tag")
    for tag in Tag.objects.iterator():
        if not tag.uuid:
            Tag.objects.filter(id=tag.id).update(uuid=uuid.uuid4())


class Migration(migrations.Migration):
    dependencies = [
        ('content', '0033_tag_uuid'),
    ]

    operations = [
        RunPython(forward, RunPython.noop)
    ]
