# Generated by Django 2.2.28 on 2022-11-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_profile_finger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='finger',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, unique=True, verbose_name='Webfinger subject'),
        ),
    ]
