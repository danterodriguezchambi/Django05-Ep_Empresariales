# Generated by Django 3.2.18 on 2023-04-23 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_puclicacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
