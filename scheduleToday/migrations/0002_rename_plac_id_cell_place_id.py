# Generated by Django 4.2.8 on 2024-01-06 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleToday', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cell',
            old_name='plac_id',
            new_name='place_id',
        ),
    ]
