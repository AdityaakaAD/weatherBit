# Generated by Django 4.0.3 on 2022-06-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0010_alter_monthlytemperature_apr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Apr',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Aug',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Dec',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Feb',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Jan',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Jul',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Jun',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Mar',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='May',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Nov',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Oct',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='monthlytemperature',
            name='Sep',
            field=models.FloatField(default=None),
        ),
    ]