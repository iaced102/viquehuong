# Generated by Django 3.2.7 on 2021-12-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_cast_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cast',
            name='note',
        ),
        migrations.AddField(
            model_name='active_order',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
