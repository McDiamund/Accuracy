# Generated by Django 2.1.1 on 2018-11-19 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0004_auto_20181119_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.Account'),
        ),
    ]
