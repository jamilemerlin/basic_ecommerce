# Generated by Django 3.0.5 on 2020-04-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('code', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
