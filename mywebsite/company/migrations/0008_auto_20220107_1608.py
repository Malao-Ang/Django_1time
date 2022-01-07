# Generated by Django 3.2 on 2022-01-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_resetpasswordtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='verify_token',
            field=models.CharField(default='No token', max_length=20),
        ),
    ]
