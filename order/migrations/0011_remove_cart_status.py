# Generated by Django 3.2.7 on 2021-12-19 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
    ]
