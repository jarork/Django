# Generated by Django 2.2.13 on 2020-08-11 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20200811_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
    ]
