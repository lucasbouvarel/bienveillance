# Generated by Django 2.1.5 on 2019-09-29 14:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('colloc', '0007_auto_20190929_1432'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['date'], 'verbose_name': 'Transaction'},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 29, 14, 47, 45, 715412, tzinfo=utc), null=True),
        ),
    ]
