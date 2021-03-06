# Generated by Django 2.2.10 on 2021-03-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_file_part_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='short_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_name',
            field=models.CharField(max_length=50),
        ),
    ]
