# Generated by Django 4.1.5 on 2023-01-29 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_stock_s_id_alter_stock_s_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='s_id',
            field=models.IntegerField(),
        ),
    ]
