# Generated by Django 3.2.18 on 2023-04-02 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_auto_no_op'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['domain'], 'verbose_name': 'site', 'verbose_name_plural': 'sites'},
        ),
    ]
