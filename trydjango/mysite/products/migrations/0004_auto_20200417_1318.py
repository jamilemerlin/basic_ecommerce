# Generated by Django 3.0.5 on 2020-04-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200407_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count_sells',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_in_stock',
            field=models.IntegerField(default=0),
        ),
    ]