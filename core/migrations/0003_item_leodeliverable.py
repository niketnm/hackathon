# Generated by Django 3.0.8 on 2020-07-25 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200724_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='leodeliverable',
            field=models.BooleanField(default=False),
        ),
    ]
