# Generated by Django 3.2.9 on 2021-12-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artelApp', '0006_auto_20211226_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exports',
            name='export_year_after',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='exports',
            name='export_year_before',
            field=models.DateField(),
        ),
    ]
