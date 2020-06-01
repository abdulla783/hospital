# Generated by Django 3.0.6 on 2020-05-27 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0012_auto_20200527_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='attandance',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Onchology', 'Onchology'), ('Neurology', 'Neurology'), ('Ortho', 'Ortho'), ('Cardiology', 'Cardiology')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='salary',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='casepaper',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='outstanding',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='paid',
            field=models.PositiveIntegerField(default=0),
        ),
    ]