# Generated by Django 3.0.6 on 2020-05-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0009_prescription_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
