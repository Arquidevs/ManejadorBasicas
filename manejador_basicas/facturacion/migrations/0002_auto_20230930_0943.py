# Generated by Django 3.2.6 on 2023-09-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_factura', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
    ]
