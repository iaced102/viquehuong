# Generated by Django 4.0.1 on 2022-01-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_active_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='active_order',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
