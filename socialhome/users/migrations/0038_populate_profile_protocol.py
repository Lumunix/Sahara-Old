# Generated by Django 2.0.13 on 2019-03-17 19:16

from django.db import migrations
from django.db.migrations import RunPython


def forward(apps, schema_editor):
    Profile = apps.get_model("users", "Profile")
    Profile.objects.filter(protocol="").update(protocol="diaspora")


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_profile_protocol'),
    ]

    operations = [
        RunPython(forward, RunPython.noop)
    ]
