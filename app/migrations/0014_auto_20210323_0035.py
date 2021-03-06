# Generated by Django 2.2.10 on 2021-03-22 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210320_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('contact', models.IntegerField(max_length=10, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('pan', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50, null=True)),
                ('weight', models.IntegerField(max_length=10, null=True)),
                ('charge_per_gram', models.IntegerField(max_length=10, null=True)),
                ('item_description', models.CharField(max_length=200, null=True)),
                ('availability', models.IntegerField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(blank=True, null=True)),
                ('updated_date', models.DateField(blank=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('order_amount', models.IntegerField(max_length=10, null=True)),
                ('discount', models.IntegerField(max_length=10, null=True)),
                ('tax_amount', models.IntegerField(max_length=10, null=True)),
                ('order_details', models.CharField(max_length=200, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_weight', models.IntegerField(max_length=10, null=True)),
                ('rate_per_gram', models.IntegerField(max_length=10, null=True)),
                ('making_charge', models.IntegerField(max_length=10, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(max_length=10, null=True)),
                ('remarks', models.CharField(max_length=200, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Order')),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='file',
            name='section',
        ),
        migrations.RemoveField(
            model_name='filemovement',
            name='file',
        ),
        migrations.RemoveField(
            model_name='filemovement',
            name='puc',
        ),
        migrations.RemoveField(
            model_name='filemovement',
            name='put_up_by',
        ),
        migrations.RemoveField(
            model_name='filemovement',
            name='section_from',
        ),
        migrations.RemoveField(
            model_name='filemovement',
            name='section_to',
        ),
        migrations.RemoveField(
            model_name='puc',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='puc',
            name='file',
        ),
        migrations.RemoveField(
            model_name='puc',
            name='section',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='FileMovement',
        ),
        migrations.DeleteModel(
            name='PUC',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
