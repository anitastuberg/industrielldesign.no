# Generated by Django 2.2.24 on 2021-10-15 12:06

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20210202_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
