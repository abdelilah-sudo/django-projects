# Generated by Django 5.1.4 on 2025-01-03 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2025, 1, 3, 9, 8, 14, 2687)),
        ),
    ]
