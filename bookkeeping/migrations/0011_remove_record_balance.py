# Generated by Django 2.1.1 on 2018-11-20 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0010_auto_20181120_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='balance',
        ),
    ]
