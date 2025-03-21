# Generated by Django 5.1.6 on 2025-03-17 17:40

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=100, null=True)),
                ('mname', models.CharField(blank=True, max_length=100, null=True)),
                ('lname', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('party', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='logo/')),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='photo/')),
                ('aadhaar', models.CharField(blank=True, max_length=100, null=True)),
                ('proof', models.FileField(blank=True, null=True, upload_to='proof/')),
                ('voterid', models.FileField(blank=True, null=True, upload_to='voterid/')),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('mail', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Officer_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('mailid', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='photo/')),
                ('LOGIN_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.login_model')),
            ],
        ),
        migrations.CreateModel(
            name='User_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.CharField(blank=True, max_length=100, null=True)),
                ('mailid', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('mobno', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='photo/')),
                ('aadhaar', models.CharField(blank=True, max_length=100, null=True)),
                ('voterid', models.CharField(blank=True, max_length=100, null=True)),
                ('LOGIN_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.login_model')),
                ('ward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.ward')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='UserCandidateCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.CharField(max_length=10, unique=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.candidate_model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroupMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.usergroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_id', models.CharField(editable=False, max_length=100, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('previous_hash', models.CharField(blank=True, max_length=64, null=True)),
                ('vote_hash', models.CharField(blank=True, editable=False, max_length=64)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.candidate_model')),
                ('voter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Vote_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.candidate_model')),
                ('vote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Candidatecode_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.candidate_model')),
                ('voter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.user_model')),
                ('ward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.ward')),
            ],
        ),
        migrations.AddField(
            model_name='candidate_model',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Evoteapp.ward'),
        ),
    ]
