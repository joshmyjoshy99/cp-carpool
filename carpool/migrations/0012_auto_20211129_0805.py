# Generated by Django 3.2.7 on 2021-11-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0011_auto_20211128_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerride',
            name='carnames',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='offerride',
            name='seatno',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
