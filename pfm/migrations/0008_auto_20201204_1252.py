# Generated by Django 3.1.3 on 2020-12-04 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfm', '0007_auto_20201204_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfmtest',
            name='testingDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 4, 12, 52, 11, 430253)),
        ),
    ]
