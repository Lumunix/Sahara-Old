# Generated by Django 2.0.13 on 2019-03-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_populate_profile_federation_inboxes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='protocol',
            field=models.CharField(blank=True, max_length=20, verbose_name='Protocol'),
        ),
    ]
