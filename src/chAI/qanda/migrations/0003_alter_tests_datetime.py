# Generated by Django 4.1.4 on 2022-12-24 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qanda", "0002_tests_datetime_alter_tests_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tests",
            name="dateTime",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
