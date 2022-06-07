# Generated by Django 3.2 on 2022-06-06 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_alter_apartment_options'),
        ('accounts', '0004_alter_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('aIDX', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.apartment', verbose_name='아파트')),
                ('uIDX', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='회원')),
            ],
            options={
                'verbose_name': '장바구니',
                'verbose_name_plural': '장바구니 목록',
            },
        ),
    ]