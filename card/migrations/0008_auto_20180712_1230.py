# Generated by Django 2.0.7 on 2018-07-12 07:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_auto_20180711_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetails',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 12, 7, 0, 49, 527068, tzinfo=utc), verbose_name='date published'),
        ),
    ]
