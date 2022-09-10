# Generated by Django 3.2.15 on 2022-09-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('number',), 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Порядковый номер'),
        ),
    ]
