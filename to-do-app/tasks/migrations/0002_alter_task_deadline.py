# Generated by Django 5.1.4 on 2025-01-02 03:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2025, 1, 2, 3, 30, 2, 273103)),
        ),
    ]
