# Generated by Django 2.1.5 on 2019-03-28 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculdej', '0013_auto_20190329_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='det',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dossier',
            name='imc',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dossier',
            name='mb',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
    ]
