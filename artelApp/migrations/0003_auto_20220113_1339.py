# Generated by Django 3.2.9 on 2022-01-13 08:39

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artelApp', '0002_auto_20220113_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good_images',
            options={'verbose_name': 'Изображение продукту', 'verbose_name_plural': '2.2 Продукты -> Изображении '},
        ),
        migrations.AlterField(
            model_name='good_section',
            name='section_name_ru',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None, verbose_name='Секции Рус'),
        ),
        migrations.AlterField(
            model_name='good_section',
            name='section_name_tr',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, null=True, size=None, verbose_name='Секции Тур'),
        ),
        migrations.AlterField(
            model_name='good_section',
            name='section_name_us',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), blank=True, null=True, size=None, verbose_name='Секции Анг'),
        ),
        migrations.AlterField(
            model_name='good_section',
            name='section_name_uz',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None, verbose_name='Секции Узб'),
        ),
        migrations.AlterField(
            model_name='good_section_description',
            name='good_section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artelApp.goods', verbose_name='Название раздела'),
        ),
        migrations.AlterField(
            model_name='good_section_description',
            name='section_description_ru',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None, verbose_name='Описание Рус'),
        ),
        migrations.AlterField(
            model_name='good_section_description',
            name='section_description_tr',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None, verbose_name='Описание Тур'),
        ),
        migrations.AlterField(
            model_name='good_section_description',
            name='section_description_us',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None, verbose_name='Описание Анг'),
        ),
        migrations.AlterField(
            model_name='good_section_description',
            name='section_description_uz',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None, verbose_name='Описание Узб'),
        ),
    ]