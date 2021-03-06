# Generated by Django 3.0.6 on 2020-05-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0004_auto_20200525_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
