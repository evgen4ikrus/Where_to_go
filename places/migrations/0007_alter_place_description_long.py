# Generated by Django 3.2.15 on 2022-09-10 19:48

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20220910_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Подробное описание'),
        ),
    ]
