# Generated by Django 3.2 on 2021-09-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_rename_price_product_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cost',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
