# Generated by Django 4.1.5 on 2023-02-10 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_servicesimage'),
        ('orders', '0006_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='img',
            field=models.ForeignKey(blank=True, default=16, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.servicesimage'),
        ),
    ]
