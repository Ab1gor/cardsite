# Generated by Django 2.0.6 on 2018-07-05 06:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_auto_20180704_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetails',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 5, 6, 36, 45, 624114, tzinfo=utc), verbose_name='date published'),
        ),
    ]
