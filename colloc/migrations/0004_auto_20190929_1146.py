# Generated by Django 2.1.5 on 2019-09-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colloc', '0003_transaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Transaction'},
        ),
        migrations.AddField(
            model_name='transaction',
            name='point',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
