# Generated by Django 3.0.6 on 2020-05-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0010_prescription_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='patient',
        ),
        migrations.AddField(
            model_name='prescription',
            name='patient',
            field=models.ManyToManyField(null=True, to='Hospital.Patient'),
        ),
    ]
