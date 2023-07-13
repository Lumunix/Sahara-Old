# Generated by Django 2.1.9 on 2019-07-14 23:30

from django.db import migrations
from django.db.migrations import RunPython


def get_root(content):
    if content.parent:
        return get_root(content.parent)
    return content


def forward(apps, schema_editor):
    Content = apps.get_model("content", "Content")
    for content in Content.objects.filter(parent__isnull=False).iterator():
        Content.objects.filter(id=content.id).update(root_parent=get_root(content))


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0036_add_root_parent_to_content'),
    ]

    operations = [
        RunPython(forward, RunPython.noop),
    ]
