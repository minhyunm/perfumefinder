# Generated by Django 3.1.3 on 2020-12-04 02:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfm', '0003_pfmtest_testingdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='PfmList',
            fields=[
                ('list_idx', models.AutoField(primary_key=True, serialize=False)),
                ('brand_kor', models.TextField()),
                ('name_kor', models.TextField()),
                ('accords', models.TextField()),
                ('notes', models.TextField()),
                ('longevity_rate', models.DecimalField(decimal_places=3, max_digits=4)),
                ('sillage_rate', models.DecimalField(decimal_places=3, max_digits=4)),
                ('male', models.BigIntegerField()),
                ('female', models.BigIntegerField()),
                ('rating_score', models.DecimalField(decimal_places=3, max_digits=4)),
                ('brand_eng', models.TextField()),
                ('name_eng', models.TextField()),
                ('votes', models.BigIntegerField()),
                ('dates', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 4, 11, 26, 36, 378496))),
            ],
        ),
        migrations.AlterField(
            model_name='pfmtest',
            name='testingDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 4, 11, 26, 36, 378496)),
        ),
    ]