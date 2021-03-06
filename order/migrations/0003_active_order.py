# Generated by Django 3.2.7 on 2021-11-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211109_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='active_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('customer_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('tortal_price', models.CharField(max_length=30)),
                ('list_order', models.ManyToManyField(to='order.Order')),
            ],
        ),
    ]
