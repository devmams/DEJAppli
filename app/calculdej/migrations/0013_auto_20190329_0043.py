# Generated by Django 2.1.5 on 2019-03-28 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculdej', '0012_auto_20190324_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossier',
            name='det',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='dossier',
            name='imc',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='dossier',
            name='mb',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='dossier',
            name='niveau',
            field=models.CharField(default='', max_length=20),
        ),
    ]
