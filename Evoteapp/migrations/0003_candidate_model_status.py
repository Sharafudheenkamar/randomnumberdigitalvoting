# Generated by Django 5.1.6 on 2025-03-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evoteapp', '0002_user_model_voter_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate_model',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
