# Generated by Django 2.2.10 on 2021-03-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210308_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='part_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
