# Generated by Django 3.2 on 2022-06-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', '남자'), ('W', '여자')], max_length=20),
        ),
    ]
