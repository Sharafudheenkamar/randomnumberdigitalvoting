# Generated by Django 5.1.6 on 2025-03-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evoteapp', '0004_alter_complaint_model_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint_model',
            name='date',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
    ]
