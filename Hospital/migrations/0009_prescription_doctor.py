# Generated by Django 3.0.6 on 2020-05-27 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0008_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.Doctor'),
        ),
    ]
