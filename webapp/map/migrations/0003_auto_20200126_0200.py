# Generated by Django 3.0.2 on 2020-01-26 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20200126_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryitem',
            name='icon',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='queryitem',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='queryitem',
            name='query_parameter',
            field=models.CharField(max_length=64),
        ),
    ]
