# Generated by Django 4.2 on 2024-06-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('franquicias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franquicia',
            name='gerente',
            field=models.CharField(max_length=100),
        ),
    ]
