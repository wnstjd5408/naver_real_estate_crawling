# Generated by Django 3.2 on 2022-06-02 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_apartment_location_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='location_id',
            new_name='location',
        ),
    ]