# Generated by Django 2.2.24 on 2021-10-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_auto_20210910_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='intro',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
