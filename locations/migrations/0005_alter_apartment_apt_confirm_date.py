# Generated by Django 3.2 on 2022-06-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20220603_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='apt_confirm_date',
            field=models.DateTimeField(),
        ),
    ]