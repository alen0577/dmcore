# Generated by Django 4.1.7 on 2023-06-19 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0050_correction_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email_id', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('ph_no', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('location', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('qualification', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('year_of_passout', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('collegename', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('internship', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('internship_institute', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('internship_topic', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('internship_start', models.DateField(blank=True, null=True)),
                ('internship_end', models.DateField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('fresher_experience', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('previous_experience', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('register', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('followup_dt', models.DateField(blank=True, null=True)),
                ('assign_status', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('assign_dt', models.DateField(blank=True, null=True)),
                ('executive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DMcoreapp.user_registration')),
            ],
        ),
    ]
