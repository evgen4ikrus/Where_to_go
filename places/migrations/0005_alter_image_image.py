# Generated by Django 3.2.15 on 2022-09-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Картинка'),
        ),
    ]