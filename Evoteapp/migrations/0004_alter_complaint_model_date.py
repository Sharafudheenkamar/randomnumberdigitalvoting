# Generated by Django 5.1.6 on 2025-03-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evoteapp', '0003_candidate_model_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint_model',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
