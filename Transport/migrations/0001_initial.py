# Generated by Django 3.0.8 on 2020-07-26 14:25

import Children.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('School', '0003_school_admin_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Employee's First Name", max_length=120, verbose_name='Firt Name')),
                ('last_name', models.CharField(help_text="Employee's Last Name", max_length=120, verbose_name='Last Name')),
                ('phone', models.CharField(help_text="Employee's phone number", max_length=10, validators=[Children.validators.phoneVerify], verbose_name='Phone')),
                ('email', models.EmailField(help_text="Employee's Email", max_length=254, unique=True, verbose_name='Email')),
                ('address', models.TextField(help_text="Employee's Complete Address", verbose_name='Address')),
                ('country', models.CharField(max_length=120, verbose_name='County')),
                ('state', models.CharField(max_length=120, verbose_name='State')),
                ('city', models.CharField(max_length=120, verbose_name='City')),
                ('job', models.CharField(max_length=120, verbose_name='Job Profile')),
                ('verified', models.BooleanField(default=False, verbose_name='Account Verifed')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employeeAuth', to=settings.AUTH_USER_MODEL, verbose_name="Employee's Auth")),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employeeSchool', to='School.School', verbose_name='School')),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
            },
        ),
    ]
