# Generated by Django 5.1.2 on 2024-10-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='calendar',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
