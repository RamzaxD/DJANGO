# Generated by Django 4.1.7 on 2023-04-01 16:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_rename_description_project_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-tittle'], 'verbose_name': 'Proyecto'},
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tittle',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]