# Generated by Django 3.2.20 on 2023-10-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customuser_friend_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='posts_count',
            field=models.IntegerField(default=0),
        ),
    ]
