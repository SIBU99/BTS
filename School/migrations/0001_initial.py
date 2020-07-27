# Generated by Django 3.0.8 on 2020-07-26 13:27

import Children.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="School's Name", max_length=120, verbose_name='Name')),
                ('phone', models.CharField(help_text="School's phone number", max_length=10, validators=[Children.validators.phoneVerify], verbose_name='Phone')),
                ('email', models.EmailField(help_text="School's Email", max_length=254, unique=True, verbose_name='Email')),
                ('address', models.TextField(help_text="School's Complete Address", verbose_name='Address')),
                ('country', models.CharField(max_length=120, verbose_name='County')),
                ('state', models.CharField(max_length=120, verbose_name='State')),
                ('city', models.CharField(max_length=120, verbose_name='City')),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
            },
        ),
    ]
