# Generated by Django 3.2.20 on 2023-10-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20231015_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='friend_count',
            field=models.IntegerField(default=0),
        ),
    ]
