# Generated by Django 3.2.15 on 2022-09-06 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
