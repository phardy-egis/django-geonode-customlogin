# Generated by Django 3.2.19 on 2023-06-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customlogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='orderidx',
            field=models.IntegerField(default=0, verbose_name='Index of order (items are sorted in ascending order)'),
        ),
    ]
