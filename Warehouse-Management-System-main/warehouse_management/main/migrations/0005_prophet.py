# Generated by Django 4.1.5 on 2023-01-29 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_quantity_sq_s_in_sq_s_out'),
    ]

    operations = [
        migrations.CreateModel(
            name='prophet',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50)),
                ('p_date', models.DateField()),
                ('p_out', models.IntegerField()),
            ],
        ),
    ]
