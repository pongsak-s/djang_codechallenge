# Generated by Django 3.0.4 on 2021-10-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(default='Thai', max_length=20),
        ),
    ]
