# Generated by Django 2.0 on 2019-01-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculdej', '0008_auto_20190130_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossier',
            name='de',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
